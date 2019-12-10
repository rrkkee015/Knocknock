<template>
	<div>
		<v-list 
			v-if="selectedStores.length"
			flat 
			class="storelist py-0"
		>
			<p class="notice text-center">반경 {{ storeSearchDistance }}m 내에 운영중인 매장입니다!</p>
			<v-list-item 
				v-for="(store, idx) in selectedStores"
				:key=idx
				@click="goToWithParam('store-detail', store.id)"
				class="d-block px-0 py-1"
			>
				<StoreCard 
					:store="store" 
					:lessThanAnHour="false"	
				/>
				<v-divider 
					v-if="idx != selectedStores.length -1"
					class="mt-1"
				></v-divider>
			</v-list-item>
		</v-list>
		
		<div v-else>
			<div class="text-center mt-12">
				<v-icon class="exclamation-outline">mdi-exclamation</v-icon>
				<p class="charcoal--text">검색한 조건 내에 운영중인 업체가 없어요.</p>
			</div>
			<div class="text-center">
				<v-btn 
					@click="goTo('question')"
					outlined
					class="mt-2"
				>
					새로운 업체 등록 요청하기
				</v-btn>	
			</div>
		</div>
	</div>
</template>

<script>
import StoreCard from './StoreCard'
import router from '../../router'
import { mapState, mapMutations } from 'vuex'

export default {
	data() {
		return {
			filteringStores: [],
			selectedStores: this.stores,
		}
	},
	components: {
		StoreCard,
	},
	computed: {
		...mapState('category', ['selectedCategory']),
		...mapState('store', ['stores', 'storeSearchDistance']),
	},
	watch: {
		selectedCategory: {
			deep: true,
			handler() {
				this.filterByCategory()
			}
		},
		stores: {
			deep: true,
			handler() {
				this.filterByCategory()
			}
		}
	},
	created() {
		this.filterByCategory()
	},
	methods: {
		filterByCategory() {
			if (this.stores.length && this.selectedCategory.length) { 
				this.filteringStores = []
				var store = {}
				for (var i=0; store=this.stores[i]; i++) {
					if (this.selectedCategory.includes(store.category.sub_category)) {
						this.filteringStores.push(store)
					}
				} 
			}
			this.selectStores()
		},
		selectStores() {
			this.selectedStores = this.stores
			if (this.selectedCategory.length) {
				this.selectedStores = this.filteringStores
			} else {
				this.selectedStores = this.stores
			} 
		},
		goToWithParam(path, param) {
			router.push({ name: path, params:{ storeId: param } });
    },
		goTo(path) {
			router.push({ name: path });
    },
	}
}
</script>

<style scoped>
.storelist {
	height: 38vh;
	overflow: auto;
	border-radius: 5px;
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
</style>