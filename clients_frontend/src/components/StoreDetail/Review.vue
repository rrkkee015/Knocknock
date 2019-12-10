<template>
	<div class="px-5 py-2">
		<div class="d-flex justify-center">
			<v-btn 
				@click="registerReview"
				text
				outlined
				color="primary"
				class="my-2 px-12"
			>
				리뷰 남기기
			</v-btn>
		</div>

		<RegisterReview />
		
		<div v-if="reviews.length">
			<v-card
				v-for="(review, idx) in reviews"
				:key="idx"
				flat
				class="mb-3"
			>
				<div class="d-flex">
					<v-card-title 
						class="review-author"
					>
						{{ review.author }}
					</v-card-title>
					<v-spacer></v-spacer>
					<v-menu 
						v-if="review.client === email"
						bottom 
						left
					>
						<template v-slot:activator="{ on }">
							<v-btn
								icon
								v-on="on"
								class="mt-2 mx-2"
							>
								<v-icon>mdi-dots-vertical</v-icon>
							</v-btn>
						</template>
						<v-list>
							<v-list-item @click="goTowithParams('modify-review', review.id)">
								<v-list-item-title>수정</v-list-item-title>
							</v-list-item>
							<v-list-item @click="turnonDeleteDialog(review.id)">
								<v-list-item-title>삭제</v-list-item-title>
							</v-list-item>
						</v-list>
					</v-menu>
				</div>
				<v-card-subtitle class="py-0">
					{{ review.createdAt }}
				</v-card-subtitle>
				<v-card-text class="pa-4 black--text">
					<p class="body-1">
						{{ review.content }}
					</p>
				</v-card-text>
				<!-- feedbacks -->
				<div
					v-for="(feedback, fbIdx) in review.feedbacks"
					:key="fbIdx"
				>
					<div 
						v-if="fbIdx === 0"
						class="partner-message"
					>
						<p class="partner-name">
							사장님
						</p>
						<p class="my-1">{{ feedback.content }}</p>
					</div>
					<div 
						v-else
						class="partner-message2">
						<p class="my-1">{{ feedback.content }}</p>
					</div>
				</div>
			</v-card>
		</div>
		<div v-else>
			<p class="none-content">등록된 리뷰가 없어요.</p>
		</div>

		<!-- Login Modal -->
		<v-dialog
			v-model="loginDialog"	
			max-width="290"
		>
			<v-card class="text-center">
				<p class="pt-5">
          로그인이 필요한 서비스입니다. 
        </p>
				<v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-3"
            text
            @click="loginDialog=false"
          >
            닫기
          </v-btn>
          <v-btn
            color="blue darken-3"
            text
            @click="goTo('auth')"
          >
            로그인
          </v-btn>
        </v-card-actions>
			</v-card>
		</v-dialog>

		<!-- Delete Check Modal -->
		<v-dialog
      v-model="deleteDialog"
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
            @click="deleteDialog=false"
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
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
import router from '../../router'
import RegisterReview from './RegisterReview'

export default {
	components: {
		RegisterReview
	},
	data() {
		return {
			deleteDialog: false,
			deleteReviewId: 0,
			loginDialog: false,
		}
	},
	computed: {
		storeId() {
			return this.$route.params.storeId
		},
		...mapState('review', ['reviews']),
		...mapState('auth', ['email']),
	},
	created() {
		this.getStoreReviews(this.storeId)
	},
	methods: {
		...mapMutations('toggle', ['toggleRegisterReviewModal']),
		goTo(path) {
			router.push({ name: path });
		},
		goTowithParams(path, params) {
			router.push({ name: path, params:{ reviewId: params} });
		},
		...mapActions('review', ['getStoreReviews']),
		registerReview () {
			if (this.email) {
				this.toggleRegisterReviewModal(true)
			} else {
				this.loginDialog = true
			}
		},
		turnonDeleteDialog(reviewId) {
			this.deleteReviewId = reviewId
			this.deleteDialog = true
		},
		...mapActions('review', ['deleteReview']),
		deleteReviews() {
			this.deleteReview(this.deleteReviewId).then(() => {
				this.getStoreReviews(this.storeId)
				return this.reviews
			})
			this.deleteDialog = false

		}
	}
}
</script>

<style scoped>
.review {
	font-size: 16px;
	font-weight: 700;
}
.review-btn{
	font-weight: 700;
	font-size: 16px;
}
.none-content {
	font-size: 14px;
	color: grey;
	padding-left: 20px;
}
.review-author {
	padding-bottom: 0;
	font-weight: 600;
	font-size: 16px !important;
}
.partner-name {
	font-weight: bold;
	margin: 5px 0;
}
.partner-message {
  position: relative;
  display: inline-block;
  background-color: #eee;
  border-radius: 15px;
  padding: 8px 15px;
  margin: 0 0 5px 10px;
	max-width: 90vw;
}
.partner-message2 {
  position: relative;
  display: inline-block;
  background-color: #eee;
  border-radius: 15px;
  padding: 8px 15px;
  margin: 0 0 5px 10px;
	max-width: 90vw;
}
.partner-message:before {
  content: "";
  position: absolute;
  z-index: 0;
	top: -20px;
  left: 15px;
  height: 20px;
  width: 20px;
  background:#eee;
  border-top-left-radius: 100px;
}
.partner-message:after {
  content: "";
  position: absolute;
  z-index: 1;
	top: -20px;
  left: 27px;
  width: 10px;
  height: 20px;
  background: white;
  border-top-left-radius: 10px;
}
</style>