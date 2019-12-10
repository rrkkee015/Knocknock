<template>
	<div class="pa-6">
		<div class="pl-1">
			<span class="store-title">{{ review.storeName }}</span>
			<v-btn icon>
				<v-icon class="grey--text">mdi-chevron-right</v-icon>
			</v-btn>
		</div>
		<div>
			<p class="createdat">{{ review.createdAt }}</p>
		</div>
		<div>
			<v-textarea
				v-model="content"
				outlined
				counter
				maxlength="300"
				class="mb-0 pt-2"
			></v-textarea>
		</div>
		<div>
			<v-btn
				@click="modify"
				icon
				color="primary"
				class="review-btn"	
			>
				수정
			</v-btn>
			<v-divider
				vertical 
				class="vertical-divider"
			></v-divider>
			<v-btn 
				@click="goTo"
				icon	
				class="review-btn"	
			>
				취소
			</v-btn>
		</div>
	</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import router from '../../router'

export default {
	data() {
		return {
			reviewId: 0,
			editContent: '없음'
		}
	},
	computed: {
		...mapState('review', ['review']),
		content: {
			get() {
				return this.review.content
			},
			set(value) {
				this.editContent = value
			}
		}
	},
	created() {
		this.reviewId = this.$router.app._route.params.reviewId
	},
	async mounted() {
		await this.getReview(this.reviewId)
	},
	methods: {
		...mapActions('review', ['getReview', 'modifyReview']),
		goTo() {
			router.go(-1)
		},
		modify() {
			var params = {
				'reviewId': this.review.id,
				'content': this.editContent
			}
			this.modifyReview(params).then(() => {
				router.go(-1)
			})
		}
	}
}
</script>

<style scoped>
.store-title {
	font-size: 20px;
	font-weight: 500;
	vertical-align: middle;
}
.review-rating {
	display: inline-block;
}
.review-btn {
	font-weight: 600;
	text-align: left;
}
.vertical-divider {
	color: black; 
	height: 15px;
	margin: 0 10px;
}
.createdat {
	color: grey;
	font-size: 14px;
	margin-bottom: 0;
}
</style>