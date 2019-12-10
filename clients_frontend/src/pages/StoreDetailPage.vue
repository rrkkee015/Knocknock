<template>
	<div>
		<StoreInfoSummary />
		<div class="divide-box"></div>
		<StoreInfo />
	</div>
</template>

<script>
import StoreInfoSummary from '../components/StoreDetail/StoreInfoSummary'
import StoreInfo from '../components/StoreDetail/StoreInfo'
import { mapMutations, mapActions } from 'vuex'

export default {
	components: {
		StoreInfoSummary,
		StoreInfo
	},
	created() {
		this.storeId = this.$router.app._route.params.storeId
	},
	mounted() {
		this.getSingleStore(this.storeId)
		this.setCategory('init')
	},
	destroyed() {
		this.setSingleStore({
			options: [],
			reviews: {
				feedbacks: []
			},
			tags: [],
			menus: [],
		})
	},
	methods: {
		...mapActions('store', ['getSingleStore']),
		...mapMutations('store', ['setSingleStore']),
		...mapMutations('category', ['setCategory']),
	}
}
</script>

<style scoped>
.divide-box {
	width: 100%; 
	height: 30px; 
	background-color: whitesmoke;
}
</style>