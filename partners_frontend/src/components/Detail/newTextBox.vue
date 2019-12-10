<template>
  <div class="mt-5">
    <div class="newPost-layout mb-4">
      <div class="pa-5">
        <p class="newPost-title mb-0">제목</p>
        <v-text-field
          class="text-area-font"
          v-model="newPostTitle"
        >
        </v-text-field>
        <p class="newPost-title mb-0">내용</p>
        <v-textarea
          class="text-area-font"
          v-model="newPostContent"
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
export default {
  data () {
    return {
      newPostTitle: '',
      newPostContent: ''
    }
  },
  methods: {
    submit () {
    }
  }
}
</script>

<style scoped>
.newPost-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.newPost-title {
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
