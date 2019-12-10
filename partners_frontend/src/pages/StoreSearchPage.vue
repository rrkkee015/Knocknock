<template>
  <div>
    <v-col cols="12" class="register-head">영업장 검색</v-col>
    <v-col class="info-text py-0">관리하실 영업장을 <span class="emphasize-text">검색</span>하세요. <br>매장을 못 찾겠으면 <span class="emphasize-text">직접 등록</span>을 이용해주세요.</v-col>
    <v-col>
      <SearchForm/>
      <SearchResultList/>
    </v-col>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

import SearchForm from '../components/RegistStore/SearchForm'
import SearchResultList from '../components/RegistStore/SearchResultList'

export default {
  components: {
    SearchForm,
    SearchResultList
  },
  methods: {
    ...mapMutations('store', ['initSearchOn'])
  },
  beforeRouteLeave (to, from, next) {
    this.initSearchOn()
    next()
  }
}
</script>

<style scoped>
.info-text {
  font-family: 'Noto Sans KR', sans-serif;
}
.emphasize-text {
  font-weight: 500;
  color: #0091EA;
}
.register-head {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.register-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
</style>
