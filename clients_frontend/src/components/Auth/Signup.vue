<template> 
  <v-row class="justify-center padding-bottom-95">
		<v-col cols="11">
			<p class="font-weight-700 font-size-40">회원가입</p>
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
			>
			</v-text-field>
			<v-text-field
				v-model="checkPassword"
				type="password"
				outlined
				required
				placeholder="비밀번호를 한번 더 입력해주세요."
				:error-messages="checkPasswordErrors"
				@input="$v.checkPassword.$touch()"
				@blur="$v.checkPassword.$touch()"
				@keyup.enter="signup"
			>
			</v-text-field>
			<v-btn
				@click="signup"
				color="primary"
				depresseds
				block
				large
				class="font-weight-700 font-size-20"
			>
				회원가입
			</v-btn>
		</v-col>
		<v-col
			cols="12"
			class="position-bottom text-center"
		>
			<hr class="hr-light" />
			<p>낰낰 회원인가요?
				<span
					@click="backSignin"
					class="primary--text"
				>
					지금 로그인하세요.
				</span>
			</p>
		</v-col>
	</v-row>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  mixins: [validationMixin],

  validations: {
    email: {
      required,
      email
    },
    password: {
      required,
      minLength: minLength(6)
    },
    checkPassword: {
      required,
      sameAs: sameAs('password')
    }
  },
  data () {
    return {
      email: '',
      password: '',
      checkPassword: ''
    }
  },
  computed: {
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
    },
    checkPasswordErrors () {
      const errors = []
      if (!this.$v.checkPassword.$dirty) {
        return errors
      };
      !this.$v.checkPassword.required && errors.push('비밀번호는 필수값입니다.')
      !this.$v.checkPassword.sameAs && errors.push('비밀번호가 일치하지 않습니다.')
      return errors
    },
    ...mapState({
      dialog: state => state.toggle.signupShow
    }),
    ...mapState('auth', ['err'])
  },
  methods: {
    ...mapMutations('toggle', ['toggleSignup']),
    ...mapMutations('auth', ['initError']),
    ...mapActions('auth', ['signUp']),
    backSignin () {
      this.$v.$reset()
      this.email = ''
      this.password = ''
      this.checkPassword = ''
      this.toggleSignup(false)
    },
    async signup () {
      this.$v.$touch()
      if (this.$v.$invalid) {
        console.log('유효성 검사에서 에러가 발견되었습니다.')
      } else {
        var info = {
          email: this.email,
          password: this.password,
          checkPassword: this.checkPassword
        }
        await this.signUp(info)
        if (!this.err) {
          this.toggleSignup(false)
          this.$emit('turnToggle')
        } else {
          this.$emit('turnToggleError')
          this.initError()
        }
      }
    }
  }
}
</script>

<style scoped>
.white-bg {
  background-color: white;
}
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
