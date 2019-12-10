<template>
	<!-- Register Review -->
	<v-dialog 
		v-model="dialog" 
		fullscreen
		hide-overlay 
		transition="dialog-bottom-transition"
	>
		<v-card>
			<v-toolbar flat>
				<v-toolbar-title class="font-weight-bold">{{ store.name }}</v-toolbar-title>
				<v-spacer></v-spacer>
				<v-btn 
					@click="turnOffDialog"
					icon 
				>
					<v-icon>mdi-close</v-icon>
				</v-btn>
			</v-toolbar>
			<v-card-text class="review">
				<div>
					<p>내용</p>
					<v-form
						ref="form"
					>
						<v-textarea
							v-model="content"
							:rules="[() => !!content || '내용을 입력해주세요']"
							counter
							maxlength="300"
							outlined
							full-width
							auto-grow
							required
							class="font-weight-medium"
						>
						</v-textarea>
					</v-form>
				</div>
			</v-card-text>
			<v-card-actions class="px-6">
				<v-btn 
					@click="registerReview"
					block
					color="primary"
					class="review-btn"
				>
					등록
				</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
 
export default {
	data() {
		return {
			rating: 0,
			content: null
		}
	},
	computed: {
		...mapState('toggle', {
			dialog: state => state.registerReviewModalShow
		}),
		...mapState('store', ['store']),
	},
	methods: {
		...mapMutations('toggle', ['toggleRegisterReviewModal']),
		turnOffDialog() {
			this.toggleRegisterReviewModal(false)
		},
		...mapActions('review', ['setReview']),
		...mapActions('review', ['getStoreReviews']),
		async registerReview() {
			var params = {
				'store': this.store.id,
				'content': this.content
			}
			if (this.content !== null) {
				await this.setReview(params)
				this.getStoreReviews(this.store.id)
				this.toggleRegisterReviewModal(false)
				this.$refs.form.reset()
			}
		}
	}
}
</script>