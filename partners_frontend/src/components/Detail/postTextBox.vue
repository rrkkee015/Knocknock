<template>
  <div class="mt-5">
    <div class="post-layout mb-4">
      <div class="pa-5">
        <p class="post-title mb-0">제목</p>
        <v-text-field
          class="text-area-font"
          v-model="postTitle"
        >
        </v-text-field>
        <p class="post-title mb-0">내용</p>
        <v-textarea
          class="text-area-font"
          v-model="postContent"
        >
        </v-textarea>
        <div class="fill-width btn-layout">
          <v-btn
            color="primary"
            dark
            small
            @click="submit()"
          >작성 완료</v-btn>  
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      newPost: '',
      newTitle: ''
    }
  },
  computed: {
    postTitle: {
      get () {
        return this.$store.state.postEvent.postTitle
      },
      set (title) {
        this.newTitle = title
      }
    },
    postContent: {
      get () {
        return this.$store.state.postEvent.postContent
      },
      set (content) {
        this.newPost = content
      }
    }
  },
  methods: {
    ...mapMutations('postEvent', ['changeTextBox', 'changeContent']),
    submit () {
      this.changeTextBox()
      this.changeContent(this.newPost)
    }
  }
}
</script>

<style scoped>
.post-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.post-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  font-weight: 700;
}
.btn-layout {
  display: flex;
  justify-content: flex-end;
}
.text-area-font {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
