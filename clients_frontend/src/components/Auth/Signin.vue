<template> 
  <v-row class="justify-center padding-bottom-95">
    <v-col cols="11">
      <p class="font-weight-700 font-size-40">낰낰</p>
      <v-text-field
        v-model="email"
        outlined
        required
        placeholder="이메일을 입력해주세요."
        :error-messages="emailErrors"
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
      >
      </v-text-field>
      <v-text-field
        v-model="password"
        type="password"
        outlined
        required
        placeholder="비밀번호를 입력해주세요."
        :error-messages="passwordErrors"
        @input="$v.password.$touch()"
        @blur="$v.password.$touch()"
        @keyup.enter="signin"

      >
      </v-text-field>
      <v-btn
        @click="signin"
        color="primary"
        depressed
        block
        large
        class="font-weight-700 font-size-20"
      >
        로그인
      </v-btn>
    </v-col>
    
    <v-col
      cols="12"
      class="position-bottom text-center"
    >
      <hr class="hr-light" />
      <p>낰낰 회원이 아닌가요?
        <span
          @click="openSignup"
          class="primary--text"
        >
          지금 가입하세요.
        </span>
      </p>
    </v-col>
  </v-row>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email, minLength } from 'vuelidate/lib/validators'
import { mapState, mapMutations, mapActions } from 'vuex'
import router from '../../router'

export default {
  mixins: [validationMixin],

  validations: {
    email: { required, email },
    password: { required, minLength: minLength(6) }
  },
  data () {
    return {
      email: '',
			password: '',
			prevRoute: null
    }
  },
  computed: {
    ...mapState('auth', ['err']),
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('이메일 형식이 아닙니다.')
      !this.$v.email.required && errors.push('이메일은 필수값입니다.')
      return errors
    },
    passwordErrors () {
      const errors = []
      if (!this.$v.password.$dirty) return errors
      !this.$v.password.minLength && errors.push('비밀번호는 6자리 이상입니다.')
      !this.$v.password.required && errors.push('비밀번호는 필수값입니다.')
      return errors
    }
  },
  methods: {
    ...mapMutations('toggle', ['toggleSignup']),
    ...mapMutations('toggle', ['toggleHeader']),
    ...mapMutations('auth', ['initError', 'logOutCondition', 'setEmail']),
    ...mapActions('auth', ['signIn']),
    openSignup () {
      this.$v.$reset()
      this.email = ''
      this.password = ''
			this.toggleSignup(true)
    },
    async signin () {
      if (this.email == '' || this.password == '') {
        this.$emit('turnToggleWrite')
      } else {
        var info = {
          email: this.email,
          password: this.password
        }
        await this.signIn(info)
        if (!this.err) {
          router.go(-1)
					this.logOutCondition()
					this.setEmail()
        } else {
          console.log('로그인 실패 ㅠㅠ')
          this.initError()
          this.$emit('turnToggleError')
        }
			}
    }
	},
	destroyed() {
		this.toggleHeader(true)
	}
}
</script>

<style scoped>
.padding-bottom-95 {
  padding-bottom: 95px;
}
.font-weight-700 {
  font-weight: 700;
}
.font-size-20 {
  font-size: 20px !important;
}
.font-size-40 {
  font-size: 40px;
}
.hr-light {
  border: 0.5px solid rgba(0, 0, 0, 0.2);
  margin-bottom: 15px;
}
.position-bottom {
  position: absolute;
  bottom: 15px;
}
</style>
