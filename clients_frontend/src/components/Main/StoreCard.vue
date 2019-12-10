<template>
	<div class="store-content">
		<span class="store-title">{{ store.name }}</span>
		<span class="store-subcategory">{{ store.subCategory }}</span>
		<div class="ellipsis">
			<p 
				class="store-remainingtime"
				:class="{ active: anHour }"	
			>
				{{ leftTime }}
			</p>
			<v-divider vertical class="divider"></v-divider>
			<p class="store-distance">{{ store.distance }}m</p>
		</div>
		<div class="ellipsis">
			<div 
				v-if="store.contact"
				class="d-inline"
			>
				<p class="store-biztel">{{ store.contact }}</p>
				<v-divider vertical class="divider"></v-divider>
			</div>
			<p 
				v-if="store.roadAddr"
				class="store-addr"
			>
				{{ store.roadAddr }}
			</p>
			<p
				v-else
				class="store-addr"
			>	
				{{ store.addr }}
			</p>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			anHour: false,
		}
	},
	props: {
		store: {
			type: Object,
			default: {}
		},
	},
	computed: {
		leftTime() {
			var leftMin = this.store.leftTime
			if (leftMin === -1) {
				this.anHour = false
				return '24시간 영업'
			} else if (leftMin < 60) {
				this.anHour = true
				return '마감 ' + leftMin + '분 전'
			} else if (leftMin % 60) {
				this.anHour = false
				return '마감 ' + parseInt(leftMin/60) + '시간 ' + leftMin%60 + '분 전'
			} else {
				this.anHour = false
				return '마감 ' + parseInt(leftMin/60) + '시간 전'
			}
		}
	}
}
</script>

<style scoped>
.store-content {
	padding: 0 15px;
}
.store-title {
	font-weight: 700; 
}
.store-subcategory {
	font-size: 14px;
	color: gray;
	padding: 10px 0 0 5px;
}
.store-remainingtime {
	display: inline;
	color: #1976D2;
}
.store-distance {
	display: inline;
	font-size: 14px;
	padding: 0;
}
.store-biztel {
	display: inline;
	font-size: 14px;
	text-decoration: none;
	color:rgb(102, 102, 102);
}
.store-addr {
	display: inline;
	font-size: 14px;	
	padding: 0;
}
.ellipsis {
	display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
.charcoal--text {
	color: rgb(102, 102, 102);
}
.exclamation-outline {
	padding: 10px;
	margin-bottom: 5px;
	border: 1px solid rgb(102, 102, 102);
	border-radius: 23px;
}
.notice {
	padding: 2px 4px;
	margin: 4px 14px;
	font-size: 13px;
	color: white; 
	background-color: grey;
}
.active {
	color: red;
}
</style>