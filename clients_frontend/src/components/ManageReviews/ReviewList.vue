<template>
	<v-container>
		<p class="font-headline">리뷰관리</p>
		<div v-if="reviews.length">
			<div
				v-for="(review, idx) in reviews"
				:key="idx"	
				class="mb-12"
			>
				<Review :review="review" />
			</div>
		</div>
		<div v-else>
			<p>등록된 리뷰가 없어요.</p>
		</div>
	</v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Review from './Review'

export default {
	components: {
		Review
	},
	computed: {
		...mapState('review', ['reviews']),
	},
	created() {
		this.getReviews()
	},
	methods: {
		...mapActions('review', ['getReviews']),
	}
}
</script>

<style scoped>
.font-headline {
  font-size: 24px;
  font-weight: 700;
}
</style>