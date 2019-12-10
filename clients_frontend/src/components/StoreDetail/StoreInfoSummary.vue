<template>
	<div>
		<div 
			v-if="store.thumbnail" 
			class="thumbnail-wrap"
		>
			<v-img 
				:src="store.thumbnail" 
				class="thumbnail" 
			/>
		</div>
		<div 
			v-else
			class="thumbnail-wrap"
		>
			<v-img src="../../assets/noThumbnail.png" />
		</div>
		<!-- Info -->
		<div class="mx-5 mt-2 mb-5">
			<div class="store-title text-center">
				<span class="store-name">{{ store.name }}</span>
				<span class="store-subcategory">{{ store.subCategory }}</span>
			</div>
			<div class="store-info text-center">
				<span>리뷰 {{ reviewsLen }}</span>
				<v-divider
					vertical 
					class="vertical-divider"
				></v-divider>
				<span>조회 {{ store.viewCnt }}</span>
				<div 
					v-if="store.contact"
					class="d-inline"
				>
					<v-divider
						vertical 
						class="vertical-divider"
					></v-divider>
					<v-icon class="store-icon mdi-18px mr-1">mdi-phone-outline</v-icon>
					<a :href="contact" class="no-underbar">{{ store.contact }}</a>
				</div>
			</div>
			<v-divider class="my-2"></v-divider>
			<v-row class="my-2">
				<v-col 
					cols="1"
					class="py-0"
				>
					<v-icon class="store-icon">mdi-clock-outline</v-icon>
				</v-col>
				<v-col 
					v-if="businessHours"
					cols="11"
					class="py-0"	
				>
					<div 
						v-for="(bizHours, idx) in businessHours"
						:key="idx"
						:class="{bold : idx===today}"
					>
					<div v-if="idx===today || idx===yesterday || idx===tomorrow">
						<div>
							<span class="mr-2">{{ bizHours.day }}</span>
							<span v-if="!bizHours.isDayoff">{{ bizHours.start.slice(0, 5) }}~{{ bizHours.end.slice(0, 5) }}</span>
							<span v-else>휴뮤일</span>
						</div>
						<div>
							<div 
								v-if="bizHours.startBreak && bizHours.endBreak"
								class="mr-2 d-inline"
							>
								<span class="mr-2">쉬는시간</span>
								<span>{{ bizHours.startBreak.slice(0, 5) }}~{{ bizHours.endBreak.slice(0, 5) }}</span>
							</div>
							<div 
								v-if="bizHours.lastOrder"
								class="mr-2 d-inline"
							>
								<span class="mr-2">마지막주문</span>
								<span>{{ bizHours.lastOrder.slice(0, 5) }}</span>
							</div>
							</div>
							<v-divider 
								v-if="idx != businessHours.length-1"
								class="mb-1">
							</v-divider>
					</div>
						
					</div>
				</v-col>
			</v-row>
			<v-row class="my-2">
				<v-col 
					cols="1"
					class="py-0"
				>
					<v-icon class="store-icon">mdi-map-marker-outline</v-icon>
				</v-col>
				<v-col 
					v-if="store.roadAddr"
					cols="11"
					class="py-0"
				>
					<span>{{ store.roadAddr }}</span>
				</v-col>
				<v-col 
					v-else
					cols="11"
					class="py-0"
				>
					<span>{{ store.addr }}</span>
				</v-col>
			</v-row>
			<v-row 
				v-if="store.priceAvg"
				class="my-2"
			>
				<v-col 
					cols="1"
					class="py-0"
				>
					<v-icon class="store-icon">mdi-coin-outline</v-icon>
				</v-col>
				<v-col 
					cols="11"
					class="py-0"
				>
					<span>{{ store.priceAvg }}원대</span>
				</v-col>
			</v-row>
			<div v-if="store.tags">
				<v-chip
					v-for="(tag, idx) in store.tags"
					:key="idx"	
					class="notice-content mx-1 mt-1"
				> 
					{{ tag }}
				</v-chip>
			</div>
		</div>
	</div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
	data() {
		return {
			snackbar: true,
			timeout: 0,
			bookmark: false,
		}
	},
	computed: {
		...mapState('store', ['store']),
		...mapGetters('store', ['reviewsLen', 'businessHours']),
		thumbnail() {
			if (store.thumbnail) {
				return store.thumbnail
			} else {
				return '../../assets/noThumbnail.png'
			}
		},
		// businessHours = [월, 화, 수, ...], Date().getDay() = [일, 월, 화, ...]라서 인덱스 맞춤
		yesterday() {
			var td = new Date().getDay()
			if (td === 0) {
				return 5
			} else if (td === 1) {
				return 6
			}
			return td - 2
		},
		today() {
			var td = new Date().getDay()
			if (td === 0) {
				return 6
			}
			return td - 1
		},
		tomorrow() {
			return new Date().getDay()
		},
		contact() {
			return 'tel:'+this.store.contact
		}
	},
	methods: {
		checkBookmark() {
			this.bookmark = !this.bookmark
		}
	}
}
</script>

<style scoped>
.thumbnail {
	width: 100%;
	height: 280px;
	object-fit: cover;
}
.store-title {
	padding: 5px;
}
.store-name {
	font-size: 28px;
}
.store-subcategory {
	color: grey;
	font-size: 14px;
	padding-left: 12px;
	word-break: keep-all;
}
.store-remaining {
	background-color: #1976d2;
	color: white;
	/* color: red; */
	font-size: 20px;
	font-weight: 700; 
	margin: 0;
	padding: 5px 10px;
}
.store-info {
	color: gray;
	font-size: 14px;
}
.vertical-divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
.store-icon {
	color: darkgray;
	margin-right: 8px;
	font: lighter;
}
.charcoal--text {
	color: rgb(102, 102, 102);
}
.bold {
	font-weight: bold;
}
.no-underbar {
	text-decoration: none;
}
</style>