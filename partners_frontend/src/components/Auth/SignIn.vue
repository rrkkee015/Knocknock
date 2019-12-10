<template>
  <v-row>
    <v-col cols="12">
      <p class="login-font mb-0">낰낰 <span>파트너</span></p>
    </v-col>
    <v-col cols="12">
      <v-text-field
        class="Noto-Sans-KR"
        label="이메일"
        v-model="email"
        outlined
        rounded
        clearable
      ></v-text-field>
      <v-text-field
        class="Noto-Sans-KR"
        label="비밀번호"
        v-model="password"
        type="password"
        outlined
        rounded
        clearable
      ></v-text-field>
    </v-col>
    <v-col class="center pt-0" cols="12">
      <v-btn class="Noto-Sans-KR" x-large color="primary" @click="signIn()">로그인 하기</v-btn>
    </v-col>
    <v-col class="Noto-Sans-KR center-also-align bottom-position fill-width">
      <span class="px-3">낰낰 파트너의 계정이 없으신가요?</span><v-btn class="signup-font" color="primary" text @click="onOff()">회원가입</v-btn>
    </v-col>
  </v-row>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import router from '../../router'

export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  computed: {
    ...mapState('auth', ['error'])
  },
  methods: {
    ...mapMutations('auth', ['onOff', 'initError', 'setUser']),
    ...mapActions('auth', ['userSignIn']),
    async signIn () {
      if (this.email == '' || this.password == '') {
        this.$emit('turnToggleWrite')
      } else {
        var info = {
          email: this.email,
          password: this.password
        }
        await this.userSignIn(info)
        if (!this.error) {
          this.setUser()
          router.push('/store')
        } else {
          console.log('로그인 실패 ㅠㅠ')
          this.initError()
          this.$emit('turnToggleError')
        }
      } 
    }
  }
}
</script>

<style scoped>
.login-font {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 72px;
  font-weight: 900;
}
.login-font > span {
  font-size: 40px;
}
.Noto-Sans-KR {
  font-family: 'Noto Sans KR', sans-serif;
}
.center {
  display: flex;
  justify-content: center;
}
.center-also-align {
  display: flex;
  justify-content: center;
  align-items: center;
}
.bottom-position {
  position: absolute;
  bottom: 12px;
}
.signup-font {
  font-weight: 600;
  font-size: 16px;
}
</style>
