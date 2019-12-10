<template>
	<div>
		<Map />
		<StoreList v-show="!filterToggle" />
		<CategoryFilter v-show="filterToggle" />
	</div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import Map from '../components/Main/Map'
import StoreList from '../components/Main/StoreList'
import CategoryFilter from '../components/Main/CategoryFilter'

export default {
  components: {
		Map,
		StoreList,
		CategoryFilter
	},
	computed: {
		...mapState('toggle', { filterToggle: ['filterShow'] }),
	},
	mounted() {
		this.toggleHeader(true)
	},
	methods: {
		...mapMutations('toggle', ['toggleHeader']),
	}
}
</script>