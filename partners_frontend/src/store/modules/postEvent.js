const state = {
  textBox: false,
  postTitle: '2019년 10월 22일 공지사항',
  postContent: '아프리카 돼지 열병 사태로 당분간 영업을 하지 않습니다. 혹시나 국밥이 마려우신 분은 성진이네 국밥가게를 가주시기 바랍니다.',
  eventTitle: '하루만 떨이 행사 !',
  eventContent: '돼지국밥을 먹으면 순대를 얹어드립니다!'
}

const mutations = {
  changeTextBox (state) {
    state.textBox = !state.textBox
  },
  changeContent (state, content) {
    state.postContent = content
  }
}

// actions만 만들면 된다.

export default {
  namespaced: true,
  state,
  mutations
}
