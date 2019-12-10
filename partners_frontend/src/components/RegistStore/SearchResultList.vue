<template>
  <div class="mt-10 section-font">
    <v-col v-if="!searchResult.length && searchOn" class="pt-0 center">
      <v-icon class="mb-2">fas fa-exclamation-circle</v-icon>
    </v-col>
    <p v-if="!searchResult.length && searchOn" class="nonText">검색한 조건을 만족하는 매장이 없습니다.<br>다시 검색해 주세요. (˃︿˂)</p>
    <v-col class="section-top pa-0" cols="12" v-for="(store, i) in searchResult" :key="i" @click="goTo(store.id)">
      <v-col cols="4" class="pa-0">
        <v-img v-if="store.thumbnail" class="thumbnail" :src="store.thumbnail"></v-img>
        <v-img v-else class="thumbnail" src="../../assets/image/noneThumbnail.png"></v-img>
      </v-col>
      <v-col cols="8" class="pa-0">
        <div class="section-title section-title-layout pb-2">
          <h3>{{ store.name }}</h3>
        </div>
        <div class="section-content-text">
          <p class="mb-0">주소: <span>{{ store.common_addr }} {{ store.addr }}</span></p>
          <p class="mb-0">전화번호: <span>{{ store.contact }}</span></p>
          <p class="mb-0">업종: <span>{{ store.category.main_category }}</span></p>
          <p class="mb-0">카테고리: <span>{{ store.category.sub_category }}</span></p>
        </div>
      </v-col>
    </v-col>
  </div>
</template>

<script>
import router from '../../router'
import { mapState, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapState('store', ['searchResult', 'searchOn'])
  },
  methods: {
    ...mapMutations('store', ['setStoreId']),
    goTo (id) {
      this.setStoreId(id)
      router.push('/store/form')
    }
  }
}
</script>

<style scoped>
.nonText {
  text-align: center;
  color: rgba(0, 0, 0, 0.54)
}
.center {
  display: flex;
  justify-content: center;
}
.nonSeciont {
  display: flex;
  justify-content: center;
}
.thumbnail {
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
.section {
  display: flex;
}
.section-top {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
  height: 10rem;
  display: flex;
  align-items: center;
}
.section-font {
  font-family: 'Noto Sans KR', sans-serif;
}
.section-title-layout {
  display: flex;
  align-items: center;
}
.section-title {
  display: flex;
}
.section-title > h3 {
  padding-right: 15px;
}
.section-content-text {
  font-size: 13px;
  font-weight: 500;
}
.section-content-text > p > span {
  color: #afafaf
}
</style>