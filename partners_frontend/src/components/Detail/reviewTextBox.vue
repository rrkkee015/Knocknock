<template>
  <div>
    <div class="comment-layout mb-4">
      <div class="pa-5">
        <p class="comment-title mb-0">댓글 작성하기</p>
        <v-textarea
          v-model="recomment"
        >
        </v-textarea>
        <div class="fill-width btn-layout">
          <v-btn
            @click="onSubmit()"
            color="primary"
            dark
            small
          >작성 완료</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: {
    comment: {
      type: Object,
      deafult: {}
    }
	},
  data () {
    return {
      recomment: ''
    }
  },
  methods: {
    ...mapActions('store', ['getReviews']),
    ...mapActions('feedback', ['postFeedBack']),
    async onSubmit() {
      let params = {
        review: this.comment.id,
        content: this.recomment
      }
      await this.postFeedBack(params)
      this.getReviews(this.$route.params.storeId)
      this.recomment = ''
      this.$emit('turnTextBoxToggle')
    }
  }
}
</script>

<style scoped>
.comment-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.comment-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  font-weight: 700;
}
.btn-layout {
  display: flex;
  justify-content: flex-end;
}
</style>
