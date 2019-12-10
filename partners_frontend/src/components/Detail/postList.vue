<template>
  <v-col>
    <div class="post-title">
      <p><v-icon class="mb-1 pr-3" color="#D32F2F">fas fa-exclamation</v-icon>공지사항</p>
      <p class="new-post" @click="newPost()">새 글 등록하기</p>
    </div>
    <newTextBox v-show="newPostBoxToggle"/>
    <v-expansion-panels
      accordion
    >
      <v-expansion-panel
        v-for="(item,i) in arr"
        :key="i"
      >
        <v-expansion-panel-header class="list-header">{{ item }}</v-expansion-panel-header>
        <v-expansion-panel-content
          class="list-header"
        >
          <p>{{ arr_content[i] }}</p>
          <div class="post-buttons">
            <v-btn class="mr-4" color="#0091EA" dark small @click="openCloseTextBox">수정하기</v-btn>
            <v-btn small color="#D32F2F" dark>삭제하기</v-btn>
          </div>
          <postTextBox
            v-show="textBoxToggle"
          />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-col>
</template>

<script>
import postTextBox from './postTextBox'
import newTextBox from './newTextBox'

export default {
  components: {
    postTextBox,
    newTextBox
  },
  data () {
    return {
      arr: ['임시 휴업', '추석 연휴 공지', '재료 변경 공지'],
      arr_content: ['개인 사정으로 3일간 임시 휴업합니다.', '저희는 추석에도 영업과 배달을 진행합니다.', '중국산 재료에서 국산 재료로 탈바꿈 했습니다.'],
      page: 1,
      textBoxToggle: false,
      newPostBoxToggle: false
    }
  },
  methods: {
    openCloseTextBox () {
      this.textBoxToggle = !this.textBoxToggle
    },
    newPost () {
      this.newPostBoxToggle = !this.newPostBoxToggle
    }
  }
}
</script>

<style scoped>
.post-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
  display: flex;
  justify-content: space-between;
}
.list-header {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
}
.post-buttons {
  display: flex;
  justify-content: flex-end;
}
.new-post {
  color: #0091EA;
  font-size: 16px;
  font-weight: 500;
}
</style>
