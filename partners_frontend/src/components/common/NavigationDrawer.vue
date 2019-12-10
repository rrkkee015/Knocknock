<template>
  <v-navigation-drawer
    class="top-index"
    width="100%"
    :value="drawerToggle"
    app
  >
    <div class="flex menu-header">
      <v-col cols="10">
        <p class="menu-title mb-0">메뉴</p>
      </v-col>
      <v-col cols="2">
        <p class="menu-text" @click="drawerOnOff()">닫기</p>
      </v-col>
    </div>
    <div>
      <v-col class="menu-inner block-one" cols="12" @click="goToStore()">
        <div class="pa-3"><v-icon class="icon">fas fa-store</v-icon></div>
        <div class="pa-1 menu-text">영업장</div>
      </v-col>
      <!-- <v-col class="menu-inner block-two" cols="12">
        <div class="pa-3"><v-icon class="icon">fas fa-comments</v-icon></div>
        <div class="pa-1 menu-text">리뷰 관리</div>
      </v-col> -->
      <v-col class="menu-inner block-three" cols="12">
        <div class="pa-3"><v-icon class="icon">fas fa-wrench</v-icon></div>
        <div class="pa-1 menu-text">공사 중</div>
      </v-col>
    </div>
    <v-col class="footer footer-text fill-width">
      <p class="user-text">{{ curUser }}</p>
      <p class="signOut-text" @click="signOut()">로그아웃</p>
      <p class="mb-2">연중무휴 고객센터 <span class="pl-4 menu-text">010-5191-0337</span></p>
      <p class="mb-0 footer-info">Copyright Hey & Nerd in Gang-Nam, All Rights Reserved.</p>
    </v-col>
  </v-navigation-drawer>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import router from '../../router'

export default {
  computed: {
    ...mapState('drawer', ['drawerToggle']),
    ...mapState('auth', ['signOutToggle', 'curUser'])
  },
  methods: {
    ...mapMutations('drawer', ['drawerOnOff']),
    ...mapMutations('auth', ['initSignOut']),
    ...mapActions('auth', ['userSignOut']),
    goToStore () {
      this.drawerOnOff()
      if (this.$router.currentRoute.name !== 'storePage') {
        router.push('/store').catch(err => {
          console.log('이동하려는 위치가 현재와 동일합니다. / ' + err.message)
        })
      }
    },
    async signOut () {
      await this.userSignOut().then(() => {
        if (this.signOutToggle === true) {
          router.push('/')
          this.initSignOut()
          this.drawerOnOff()
        } else {
          console.log('로그아웃 실패!')
        }
      })
    }
  }
}
</script>

<style scoped>
.top-index {
  z-index: 2;
}
.menu-text {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
  color: black;
}
.signOut-text {
  font-weight: 900;
}
.menu-inner > div {
  display: flex;
  justify-content: center;
}
.icon {
  color: black;
}
.menu-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.menu-header {
  margin-bottom: 3rem;
}
.flex {
  display: flex;
}
.block-one {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
}
.block-three {
  border-bottom: solid 1px #dfdfdf;
}
.block-four {
  border-bottom: solid 1px #dfdfdf;
  border-right: solid 1px #dfdfdf;
}
.block-five {
  border-bottom: solid 1px #dfdfdf;
}
.block-six {
  border-bottom: solid 1px #dfdfdf;
  border-left: solid 1px #dfdfdf;
}
.footer {
  position: absolute;
  bottom: 12px;
}
.footer > p {
  display: flex;
  justify-content: center;
}
.footer-text {
  font-family: 'Noto Sans KR', sans-serif;
  color: #7b7b7b;
}
.footer-info {
  font-size: 7px;
}
.user-text {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 500;
  color: rgba(0, 0, 0, 0.87);
}
</style>
