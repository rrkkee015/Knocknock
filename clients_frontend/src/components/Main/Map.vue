<template>
	<div>
		<v-snackbar
      v-model="geolocationSnackBar"
      color="warning"
      :timeout="2000"
      top
    >
      더 나은 사용 환경을 위해 HTTPS로 접속해주세요.
    </v-snackbar>
		<div class="mb-1 px-1 timecontrol">
			<v-btn 
				v-if="!filterToggle"
				@click="turnonFilter"
				icon
			>
				<v-icon>mdi-filter-outline</v-icon>
			</v-btn>
			<v-btn 
				v-else
				@click="turnonFilter"
				icon
			>
				<v-icon>mdi-store</v-icon>
			</v-btn>
			<v-spacer></v-spacer>
			<v-btn-toggle 
				v-model="toggle_exclusive"
				color="primary"
			>
				<v-btn @click="serveTime(0)">지금</v-btn>
				<v-btn @click="serveTime(1)">+1시간</v-btn>
				<v-btn @click="serveTime(2)">+2시간</v-btn>
				<v-btn @click="serveTime(3)">+3시간</v-btn>
			</v-btn-toggle>
		</div>

		<div class="map-wrap">
			<vue-daum-map
				:appKey="appKey"
				:center.sync="center"
				:level.sync="level"
				:mapTypeId="mapTypeId"
				:libraries="libraries"
				@load="onLoad"
				@dblclick="zoomIn"
				@click="onMapEvent($event)"
				@dragend="changedLoc"
				@zoom_changed="changedLoc"
				@bounds_changed="getAddr"
				class="map" />

			<div class="hAddr">
				<p class="ma-0">{{ this.centerAddr }}</p>
			</div>

			<div class="zoomControl radius_border">
				<v-btn 
					@click="zoomIn"
					icon
				>
					<v-icon>mdi-plus</v-icon>
				</v-btn>
				<v-divider class="color_919191"></v-divider>
				<v-btn 
					@click="zoomOut"
					icon
				>
					<v-icon>mdi-minus</v-icon>
				</v-btn>
			</div>

			<div class="gpsBtn radius_border">
				<v-btn
					@click="currentPosition"
					icon
				>
					<v-icon>mdi-crosshairs-gps</v-icon>
				</v-btn>
			</div>
		
			<transition name="fade">
				<div 
					v-if="refresh"
					@click="refreshStoreList"
					class="refreshBtn radius_border"
				>
					<v-btn>
						<v-icon>mdi-refresh</v-icon>여기에서 재탐색
					</v-btn>
				</div>
			</transition>
		</div>
	</div>
</template>

<script>
import VueDaumMap from 'vue-daum-map'
import router from '../../router'
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
	components: {
		VueDaumMap
	},
	data() {
		return {
			toggle_exclusive: 0,
			geolocationSnackBar: false,
			appKey: process.env.VUE_APP_KEY,
			center: {lat: 37.553190, lng: 126.972759},
			curLoc: {lat: 0, lng: 0},
			level: 3,
			mapTypeId: VueDaumMap.MapTypeId.NORMAL,
			libraries: ['services'],
			map: null,
			curMarker: null,
			centerAddr: '',
			refresh: false,
			markers: [],
			markerNameArr: [],
			filteringStores: [],
			selectedStores: []
		}
	},
	computed: {
		...mapState('category', ['selectedCategory']),
		...mapState('toggle', { filterToggle: ['filterShow'] }),
		...mapState('store', ['stores']),
		...mapState('map', ['preCenter', 'preStores']),
	},
	watch: {
		selectedCategory: {
			deep: true,
			handler() {
				this.selectCategory()
			}
		}
	},
	destroyed() {
		this.setPreCenter({ 'lat': this.center.lat, 'lng': this.center.lng })
	},
	methods: {
		...mapMutations('map', ['setPreCenter']),

		...mapMutations('toggle', ['toggleFilter']),
    turnonFilter() {
      this.toggleFilter(!this.filterToggle)
		},

		...mapMutations('store', ['getStoreSearchLoc', 'getStoreSearchDistance']),
		onLoad(map) {
			this.map = map
			this.initPosition()
		},
		// load 후 현재 위치 불러오기
		async initPosition() {
			if (navigator.geolocation) {
				await navigator.geolocation.getCurrentPosition((position) => {
					var lat = position.coords.latitude,
							lng = position.coords.longitude
					if (this.preCenter.lat || this.preCenter.lng) {
						this.center.lat = this.preCenter.lat
						this.center.lng = this.preCenter.lng
					} else {
						this.center.lat = lat
						this.center.lng = lng	
					}
					this.curLoc.lat = lat
					this.curLoc.lng = lng
					if (this.curMarker) {
						this.replaceCurrentMarker()
					} else {
						this.firstCurrentMarker()
					}
					this.getStoreList()
				})
			} else {
				this.geolocationSnackBar = true
				this.getStoreList()
				console.log('geolocation 사용 불가능')
			}
		},
		// gps 버튼으로 현재 위치 불러오기 
		currentPosition() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition((position) => {
					var lat = position.coords.latitude,
							lng = position.coords.longitude

					this.center.lat = lat
					this.center.lng = lng	
					this.curLoc.lat = lat
					this.curLoc.lng = lng

					if (this.curMarker) {
						this.replaceCurrentMarker()
					} else {
						this.firstCurrentMarker()
					}
				})
			
			} else {
				this.geolocationSnackBar = true
				console.log('geolocation 사용 불가능')
			}
			this.refresh = true
		},
		// 현재 위치에 첫 마커 찍기
		firstCurrentMarker() {
			var imageSrc = 'http://testrottenwifi.ito.lt/bundles/itowififront/images/my-location-icon.png',
			// var imageSrc = 'https://postfiles.pstatic.net/MjAxOTExMDFfNTgg/MDAxNTcyNTg0NTMwNTE0.1h1wrlkNV4oU9OQNNkhLCiPLFCStVb0UzFLzZInQcSQg.Kf3ps9TBjXBL1rgA76QujNCm3NNjTHQy4OM7lUPYMWMg.PNG.ejttpadml/current_marker.png?type=w773',
					imageSize = new kakao.maps.Size(70, 70),
					imageOption = {offset: new kakao.maps.Point(27, 69)}; 
			var curMarkerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
			this.curMarker = new kakao.maps.Marker({
				map: this.map,
				position: new kakao.maps.LatLng(this.curLoc.lat, this.curLoc.lng),
				image: curMarkerImage
			})
		},
		// 현재 위치로 마커 옮기기 
		replaceCurrentMarker() {
			var coords = new kakao.maps.LatLng(this.curLoc.lat, this.curLoc.lng);
			this.map.setCenter(coords);
			this.level = 3

			this.curMarker.setPosition(coords)
		},
		// 지도의 클릭한 위치 주소로 보여주기
		onMapEvent (params) {
			this.searchAddrFromCoords(params[0].latLng, this.displayCenterInfo);
		},
		// 지도의 중심 위치를 주소로 보여주기
		getAddr() {
			this.searchAddrFromCoords(this.map.getCenter(), this.displayCenterInfo);
		},
		searchAddrFromCoords(coords, callback) {
			var geocoder = new kakao.maps.services.Geocoder();
			geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);
		},
		displayCenterInfo (result, status) {
			if (status === kakao.maps.services.Status.OK) {
				var infoDiv = document.getElementById('centerAddr');
				for(var i = 0; i<result.length; i++) {
						// 행정동의 region_type 값 'H' 
						if (result[i].region_type === 'H') {
								this.centerAddr = result[i].address_name;
								break;
			}}}
		},
		// 지도 확대 축소
		zoomIn () {
			if (this.level > 1) {
				this.level -= 1
			}
		},
		zoomOut () {
			if (this.level < 14) {
				this.level += 1
			}
		},
		// '여기에서 재탐색' 버튼 누르기
		refreshStoreList() {
			this.refresh = false
			this.getStoreList()
		},
		// 지정한 시간에서 store 탐색
		...mapMutations('store', ['getStoreSearchHour']),
		serveTime(params) {
			this.refresh = false
			this.getStoreSearchHour(params)
			this.getStoreList()
		},
		...mapActions('store', ['getStores']),
		// 지정한 위치에서 store 탐색 
		async getStoreList() {
			this.getStoreSearchLoc([this.center.lat, this.center.lng])
			var distance = this.getDistance()
			this.getStoreSearchDistance(distance)
			await this.getStores()
			this.selectCategory()
		},
		// 지도 level에 따라 api요청하는 반경 바꾸기
		getDistance() {
			if (this.level < 4) {
				return 100
			} else if (this.level < 6) {
				return 300
			} else {
				return 500
			}
		},
		// category로 필터링하기 
		selectCategory() {
			if (this.stores.length && this.selectedCategory.length) { 
				this.filteringStores = []
				var store = {}
				for (var i=0; store=this.stores[i]; i++) {
					if (this.selectedCategory.includes(store.category.sub_category)) {
						this.filteringStores.push(store)
						}
					} 
				}
			this.markingStore()
		},
		// stores 불러와서 마커 찍기
		markingStore() {
			this.resetMarker()
			this.resetOverlays(this.markerNameArr)
			this.markerNameArr = []
			if (this.selectedCategory.length) {
				this.resetMarker()
				this.resetOverlays(this.markerNameArr)
				this.selectedStores = this.filteringStores
			} else if (this.stores.length) {
				this.selectedStores = this.stores
			} else {
				console.log('운영중인 매장 없음')
				return 
			}
			for (var i=0; i < this.selectedStores.length; i++) {
			var store = this.selectedStores[i],
					storeLoc = new kakao.maps.LatLng(store.lat, store.lon),
					storeMarker = new kakao.maps.Marker({
						map: this.map,
						position: storeLoc,
						clickable: true
					})
			this.markers.push(storeMarker)

			var nameOverlay = new kakao.maps.CustomOverlay({
					position: storeLoc,
					content: '<div style="color: #000; font-weight: bold; text-shadow: -2px -2px 0 #ffffff, 2px -2px 0 #ffffff, -2px 2px 0 #ffffff, 2px 2px 0 #ffffff;">'+ store.name + '</div>'
				});
			this.markerNameArr.push([storeMarker, nameOverlay])

			kakao.maps.event.addListener(storeMarker, 'click', this.makeOverListener(store.id, storeLoc));
			}
		this.setOverlays(this.map, this.markerNameArr)
	},

		// 마커 제거
		resetMarker() {
			for (var i=0; i < this.markers.length; i++) {
				this.markers[i].setMap(null);
			}
		},
		// 가게 이름오버레이 표시
		setOverlays(map, Arr) {
			for (let i=0; i<Arr.length; i++) {
				var marker = Arr[i][0],
						customOverlay = Arr[i][1]
				customOverlay.setMap(map)

			};
		},
		// 가게 이름오버레이 제거
		resetOverlays(Arr) {
			for (let i=0; i<Arr.length; i++) {
				var customOverlay = Arr[i][1]
				customOverlay.setMap(null);
			}
		},
		// 가게 상세정보 페이지로 넘어가기
		// ...mapMutations('map', ['setPreCenter']),
		makeOverListener(store, storeLoc) {
			// this.setPreCenter({ 'lat': storeLoc.Ha, 'lng': storeLoc.Ga })
			return function() {
				router.push({ name: 'store-detail', params:{ storeId: store } });
			}
		},
		// 지도의 중심좌표나 level의 변화가 있을 때, 
		changedLoc() {
			this.refresh = true
			var distance = this.getDistance()
			this.getStoreSearchDistance(distance)
			this.getStoreSearchLoc([this.center.lat, this.center.lng])
		},
	}
}
</script>

<style scoped>
.timecontrol {
  display: flex; 
  justify-content: space-between;
  /* display: inline; */
}
.timecontrol button {
  height: 36px !important;
  font-weight: bold;
}

.map-wrap {
	width: 100vw;
	height: 50vh;
}
.map {
	width: 100vw;
	height: 50vh;
}
.hAddr {
	position: absolute;
	background-color: rgba(255, 255, 255, 0.8);
	top: 105px;
	left: 10px;
	padding: 10px 10px;
	z-index: 1;
}
.zoomControl {
	position: absolute;
	top: 200px;
	right: 10px;
	z-index: 1;
	width: 40px;
	background-color: white;
	text-align: center;
}
.gpsBtn {
	position: absolute;
	top: 55vh;
	right: 10px;
	z-index: 1;
	width: 40px;
	background-color: white;
	text-align: center;
}
.refreshBtn {
	position: absolute;
	top: 55vh;
	left: 50%;
	z-index: 1;
	width: 150px;
	background-color: white;
	margin-left: -75px;
}
.radius_border {
  border: 1px solid #919191;
  border-radius: 5px;
}
.color_919191 {
	border-color: #919191 !important;
}
.customoverlay {
	color: red;
}

.fade-enter-active,
.fade-leave-active {
	transition-duration: 0.2s;
	transition-property: opacity;
	transition-timing-function: ease;
}
.fade-enter,
.fade-leave-active {
	opacity: 0
}
</style>