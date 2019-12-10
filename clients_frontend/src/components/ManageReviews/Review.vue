<template>
	<div>
		<div class="pl-1">
			<span class="store-title">
				{{ review.storeName }}
			</span>
			<v-btn 
				@click="goToStore('store-detail', review.store)"
				icon
			>
				<v-icon class="grey--text">mdi-chevron-right</v-icon>
			</v-btn>
		</div>
		<div>
			<p class="caption pl-1">{{ review.createdAt }}</p>
			<p class="mb-0 py- pl-1">{{ review.content }}</p>
		</div>
		<div>
			<v-btn
				@click="goToModify('modify-review', review.id)"
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
				@click="dialog=true"
				icon	
				color="primary"
				class="review-btn"	
			>
				삭제
			</v-btn>
		</div>
		
		<!-- Chechk Modal -->
		<v-dialog
      v-model="dialog"
      max-width="290"
    >
      <v-card class="text-center">
        <p class="pt-5">
          리뷰를 정말 삭제하시겠습니까?
        </p>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-3"
            text
            @click="dialog=false"
          >
            닫기
          </v-btn>
          <v-btn
            color="blue darken-3"
            text
            @click="deleteReviews"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
	</div>
</template>

<script>
import { mapActions } from 'vuex'
import router from '../../router'

export default {
	data() {
		return {
			dialog: false,
		}
	},
	props: {
		review: {
			type: Object,
			default: {}
		}
	},
	methods: {
		...mapActions('review', ['deleteReview', 'getReviews']),
		async deleteReviews() {
			await this.deleteReview(this.review.id)
			this.getReviews()
			this.dialog = false
		},
		goToStore(path, params) {
			router.push({ name: path, params:{ storeId: params} });
		},
		goToModify(path, params) {
			router.push({ name: path, params:{ reviewId: params} });
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
</style>