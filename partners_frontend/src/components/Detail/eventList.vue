<template>
  <v-col>
    <div class="event-title">
      <p><v-icon class="mb-1 pr-3" color="#FBC02D">fas fa-star</v-icon>이벤트</p>
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
          <div class="event-buttons">
            <v-btn class="mr-4" color="#0091EA" dark small @click="openCloseTextBox">수정하기</v-btn>
            <v-btn small color="#D32F2F" dark>삭제하기</v-btn>
          </div>
          <eventTextBox
            v-show="textBoxToggle"
          />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-col>
</template>

<script>
import eventTextBox from './eventTextBox'
import newTextBox from './newTextBox'

export default {
  components: {
    eventTextBox,
    newTextBox
  },
  data () {
    return {
      arr: ['5주년 기념!', '신 메뉴 출시 기념', '코카콜라와의 협업 행사 !!'],
      arr_content: ['2019년 10월 28일부터 10월 31일까지 반값 할인을 진행합니다.', '신 메뉴를 주문하시면 2000원 할인을 해드립니다.', '펩시콜라를 코카콜라로 변경해드립니다.'],
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
.event-title {
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
.event-buttons {
  display: flex;
  justify-content: flex-end;
}
.new-post {
  color: #0091EA;
  font-size: 16px;
  font-weight: 500;
}
</style>
