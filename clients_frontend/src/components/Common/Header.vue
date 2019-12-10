<template>
  <div v-if="toggleHeader">
    <v-app-bar 
			flat 
			fixed
			class="padding-x-0"
		>
      <v-app-bar-nav-icon 
				v-show="this.isMain"
				@click="turnonDrawer"
			>
			</v-app-bar-nav-icon>
			<v-btn
				v-show="!this.isMain"
				@click="goToBack"
				icon
				class="back-btn"
			>
				<v-icon>mdi-chevron-left</v-icon>
			</v-btn>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import router from '../../router'

export default {
	data() {
		return {
			isMain: true
		}
	},
  computed: {
    ...mapState({
      toggleHeader: state => state.toggle.headerShow,
		}),
		route() {
			return this.$route.name
		}
	},
	mounted() {
		// 새로고침할 때 유지
		if (this.route === 'main') {
			this.isMain = true
		} else {
			this.isMain = false
		}
	},
	watch: {
		route() {
			// url 변경되는지 확인
			if (this.route === 'main') {
				this.isMain = true
			} else {
				this.isMain = false
			}
		}
	},
  methods: {
    ...mapMutations('toggle', ['toggleNavDrawer']),
    turnonDrawer() {
      this.toggleNavDrawer(true)
		},
		goToBack() {
			router.go(-1)
		}
  }
}
</script>

<style scoped>
.back-btn {
	margin-right: 0px !important;
	margin-left: -12px !important;
}
</style>