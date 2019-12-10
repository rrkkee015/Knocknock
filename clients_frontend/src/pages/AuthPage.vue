<template>
  <v-container fill-height>
    <Signin
			v-show="!signupShow"
      @turnToggleError="signInErrorSnackBar=true"
      @turnToggleWrite="signInWriteSnackBar=true"
    />
    <Signup
			v-show="signupShow"
      @turnToggle="snackBar=true"
      @turnToggleError="signUpErrorSnackBar=true"
    />
    <v-snackbar
      class="Noto-Sans-KR"
      color="#0091EA"
      :timeout="1500"
      v-model="snackBar"
      top
    >
      회원가입이 완료되었습니다!!
      <v-btn
        @click="snackBar=false"
        text
      >
        닫기
      </v-btn>
    </v-snackbar>
    <v-snackbar
      class="Noto-Sans-KR"
      color="#D32F2F"
      :timeout="1500"
      v-model="signInErrorSnackBar"
      top
    >
      이메일 혹은 비밀번호가 다릅니다.
    </v-snackbar>
    <v-snackbar
      class="Noto-Sans-KR"
      color="#D32F2F"
      :timeout="1500"
      v-model="signUpErrorSnackBar"
      top
    >
      이미 존재하는 이메일입니다.
    </v-snackbar>
    <v-snackbar
      class="Noto-Sans-KR"
      color="#D32F2F"
      :timeout="1500"
      v-model="signInWriteSnackBar"
      top
    >
      이메일과 비밀번호 모두 입력해주세요.
    </v-snackbar>
  </v-container>
</template>

<script>
import Signin from '../components/Auth/Signin'
import Signup from '../components/Auth/Signup'
import { mapState, mapMutations } from 'vuex'

export default {
  data () {
    return {
      snackBar: false,
      signUpErrorSnackBar: false,
      signInErrorSnackBar: false,
      signInWriteSnackBar: false
    }
  },
  components: {
    Signin,
    Signup
	},
	computed: {
		...mapState('toggle', ['signupShow'])
	},
  mounted () {
    this.toggleHeader(false)
  },
  methods: {
    ...mapMutations('toggle', ['toggleHeader'])
  }
}
</script>
