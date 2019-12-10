<template>
  <v-col class="total-size">
    <div v-if="!allReviews.length">
      <p class="info-title pr-4">리뷰</p>
      <p class="non-text">작성된 리뷰가 없습니다. (˃︿˂)</p>
    </div>
    <div v-for="(comment, i) in allReviews" :key=i class="review-detail-category">
      <p class="review-id mb-0">
        <span class="client-color">{{ comment.client }}</span>
        <span class="review-button" @click="textBox(i)">
          <v-icon class="ml-2" color="#0091EA " small>far fa-comment</v-icon>
          <span class="ml-1 review-content-button">댓글달기</span>
        </span>
      </p>
      <p class="mb-1 review-date">{{ comment.created_at.split('T')[1].split('.')[0].split(':')[0] }}시 {{ comment.created_at.split('T')[1].split('.')[0].split(':')[1] }}분 {{ comment.created_at.split('T')[0] }}</p>
      <p class="review-content">{{ comment.content }}</p>
      <reviewTextBox
        v-show="comment.reviewTextBox"
        :comment="comment"
      />
      <reviewComment
        :comment="comment"
      />
    </div>
  </v-col>
</template>

<script>
import reviewComment from './reviewComment'
import reviewTextBox from './reviewTextBox'

import { mapState, mapActions } from 'vuex'

export default {
  components: {
    reviewComment,
    reviewTextBox
  },
  async created () {
    await this.getReviews(this.$route.params.storeId)
  },
  data () {
    return {
      textBoxToggle: false
    }
  },
  computed: {
    ...mapState('store', ['allReviews', 'oneStore'])
  },
  methods: {
    ...mapActions('store', ['getReviews']),
    textBox (commentId) {
      this.allReviews[commentId].reviewTextBox = !this.allReviews[commentId].reviewTextBox
    }
  }
}
</script>

<style scoped>
.non-text {
	color: #a9a9a9;
}
.client-color {
  color: #00ACC1
}
.info-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.total-size {
  min-height: 700px;
  font-family: 'Noto Sans KR', sans-serif;
}
.review-id {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 17px;
  font-weight: 900;
}
.review-detail-category {
  font-family: 'Noto Sans KR', sans-serif;
  margin-bottom: 16px;
}
.review-date {
  font-size: 14px;
  font-weight: 500;
  color: #afafaf
}
.review-layout-flex {
  display: flex;
  align-items: flex-end;
}
.review-menu {
  font-size: 14px;
  font-weight: 500;
  color: #00BFA5;
}
.review-content-button {
  font-size: 14px;
  font-weight: 500;
}
.review-button {
  color: #0091EA;
}
</style>
