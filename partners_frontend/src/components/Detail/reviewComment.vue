<template>
  <div>
    <div class="review-comment-layout">
      <v-col cols="1"></v-col>
      <v-col cols="11" class="partners pa-0">사장님 댓글</v-col>
    </div>
    <div class="review-comment-layout pt-1" v-if="comment.feedbacks.length === 0">
      <v-col cols="1" class="pa-0">
        <v-icon class="icon-transform" small>fas fa-reply</v-icon>
      </v-col>
      <v-col cols="11" class="pa-0 nonText">
        사장님 ! 댓글을 달아주세요 (˃︿˂)
      </v-col>
    </div>
    <div v-for="(feedback, i) in comment.feedbacks" :key=i class="review-comment-layout">
      <v-col cols="1" class="pa-0">
        <v-icon class="icon-transform" small>fas fa-reply</v-icon>
      </v-col>
      <v-col cols="10" class="pa-0 partners-comment">
        <p class="mb-0">{{ feedback.content }}</p>
        <p class="created_text">{{ feedback.created_at.split('T')[1].split('.')[0].split(':')[0] }}시 {{ feedback.created_at.split('T')[1].split('.')[0].split(':')[1] }}분 {{ feedback.created_at.split('T')[0] }}</p>
      </v-col>
      <v-col cols="1">
        <v-icon @click="submit(feedback.id)" class="fas fa-times" small></v-icon>
      </v-col>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  props: {
    comment: {
      type: Object,
      deafult: {}
    }
	},
  computed: {
    ...mapState('store', ['allFeedBacks'])
  },
  methods: {
    ...mapActions('store', ['getReviews']),
    ...mapActions('feedback', ['deleteFeedBack']),
    async submit(feedBackId) {
      await this.deleteFeedBack(feedBackId)
      this.getReviews(this.$route.params.storeId)
    }
	}
}
</script>

<style scoped>
.nonText {
  color: rgba(0, 0, 0, 0.54)
}
.created_text {
  font-size: 14px;
  color: #afafaf;
}
.partners {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.partners-comment {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  font-weight: 500;
}
.icon-transform {
  transform: rotate(-180deg)
}
.review-comment-layout {
  display: flex;
}
</style>
