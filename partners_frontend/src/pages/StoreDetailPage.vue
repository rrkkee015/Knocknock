<template>
  <div class="fill-height">
    <v-col cols="12" class="pb-1 store-title">{{ storeInfo.storeName }}</v-col>
    <v-tabs
      class="section-menu"
      fixed-tabs
      color="#0091EA"
      background-color="#fafafa"
      height="4rem"
    >
      <v-tab v-bind:style="[postToggle ? choicedMenu : justMenu]" @click="changePostToggle('post')">공지사항</v-tab>
      <v-tab v-bind:style="[eventToggle ? choicedMenu : justMenu]" @click="changePostToggle('event')">이벤트</v-tab>
    </v-tabs>
    <postList v-show="postToggle"/>
    <eventList v-show="eventToggle"/>
    <v-col class="section-none py-1">
    </v-col>
    <v-tabs
      class="section-menu"
      fixed-tabs
      color="#0091EA"
      background-color="#fafafa"
      height="4rem"
    >
      <v-tab v-bind:style="[infoToggle ? choicedMenu : justMenu]" @click="changeDetailToggle('info')">정보</v-tab>
      <v-tab v-bind:style="[menuToggle ? choicedMenu : justMenu]" @click="changeDetailToggle('menu')">메뉴</v-tab>
      <v-tab v-bind:style="[reviewToggle ? choicedMenu : justMenu]" @click="changeDetailToggle('review')">리뷰</v-tab>
    </v-tabs>
    <InfoDetail :data='storeInfo' v-show="infoToggle"/>
    <MenuDetail :data='storeInfo.id' v-show="menuToggle"/>
    <reviewDetail v-show="reviewToggle"/>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'

import InfoDetail from '../components/Detail/infoDetail'
import MenuDetail from '../components/Detail/menuDetail'
import reviewDetail from '../components/Detail/reviewDetail'
import postList from '../components/Detail/postList'
import eventList from '../components/Detail/eventList'

export default {
  components: {
    InfoDetail,
    MenuDetail,
    reviewDetail,
    postList,
    eventList
  },
  data () {
    return {
      infoToggle: true,
      menuToggle: false,
      reviewToggle: false,
      postToggle: true,
      eventToggle: false,
      choicedMenu: {
        fontWeight: 700,
        fontSize: '18px'
      },
      justMenu: {
        borderBottom: 'solid 1px #dfdfdf',
        fontSize: '16px'
      }
    }
  },
  computed: {
    ...mapState('store', ['oneStore', 'storeInfo']),
  },
  async created () {
    await this.getOneStore(this.$route.params.storeId)
		this.setInfo()
  },
  methods: {
    ...mapActions('store', ['getOneStore']),
    ...mapMutations('store', ['setInfo']),
    changeDetailToggle (check) {
      if (check === 'info') {
        this.infoToggle = true
        this.menuToggle = false
        this.reviewToggle = false
      } else if (check === 'menu') {
        this.infoToggle = false
        this.menuToggle = true
        this.reviewToggle = false
      } else {
        this.infoToggle = false
        this.menuToggle = false
        this.reviewToggle = true
      }
    },
    changePostToggle (check) {
      if (check === 'post') {
        if (this.postToggle === true) {
          this.postToggle = false
        } else {
          this.postToggle = true
          this.eventToggle = false
        }
      } else {
        if (this.eventToggle === true) {
          this.eventToggle = false
        } else {
          this.postToggle = false
          this.eventToggle = true
        }
      }
    }
  }
}
</script>

<style scoped>
.store-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 40px;
  font-weight: 900;
}
.store-rating-layout {
  display: flex;
  align-items: center;
}
.section-rating-num {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  font-size: 18px;
}
.section-none {
  background-color: #efefef
}
.post-modify-button {
  color: #0091EA;
  font-weight: 500;
}
.section-menu {
  font-family: 'Noto Sans KR', sans-serif;
}
.notice {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  font-weight: 700;
  display: flex;
  justify-content: space-between;
}
.notice-content {
  font-family: 'Noto Sans KR', sans-serif;
}
.textarea-layout {
  width: 100%;
}
</style>
