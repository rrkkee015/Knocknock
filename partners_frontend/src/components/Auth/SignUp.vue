<template>
  <v-card>
    <v-container fill-height>
      <v-row>
        <v-col class="pt-0" cols="12">
          <p class="signup-font mb-0">회원가입</p>
        </v-col>
        <v-col class="Noto-Sans-KR pb" cols="12">
          <v-text-field
            label="사업자 대표자명"
            v-model="partnerName"
            :error-messages="partnerNameErrors"
            @input="$v.partnerName.$touch()"
            @blur="$v.partnerName.$touch()"
            required
            outlined
            rounded
            clearable
            autocomplete="off"
          ></v-text-field>
          <v-text-field
            label="이메일"
            hint="이메일 형식으로 작성해주세요. (예: id@email.com/co.kr/net)"
            v-model="email"
            :error-messages="emailErrors"
            @input="$v.email.$touch()"
            @blur="$v.email.$touch()"
            required
            outlined
            rounded
            clearable
            autocomplete="off"
          ></v-text-field>
          <v-text-field
            label="휴대폰 번호"
            hint="하이픈('-')을 제외하고 작성해주세요. (예: 01012345678)"
            v-model="phoneNumber"
            :error-messages="phoneNumberErrors"
            @input="$v.phoneNumber.$touch()"
            @blur="$v.phoneNumber.$touch()"
            required
            outlined
            rounded
            clearable
            autocomplete="off"
          ></v-text-field>
          <v-text-field
            label="비밀번호"
            v-model="password"
            :error-messages="passwordErrors"
            @input="$v.password.$touch()"
            @blur="$v.password.$touch()"
            required
            type="password"
            outlined
            rounded
            clearable
          ></v-text-field>
          <v-text-field
            label="비밀번호 확인"
            v-model="passwordCheck"
            :error-messages="passwordCheckErrors"
            @input="$v.passwordCheck.$touch()"
            @blur="$v.passwordCheck.$touch()"
            required
            type="password"
            outlined
            rounded
            clearable
          ></v-text-field>
        </v-col>
        <v-col class="center pt-0" cols="12">
          <v-btn class="Noto-Sans-KR" x-large color="primary" @click="signUp">회원가입 하기</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="Noto-Sans-KR center-also-align bottom-position fill-width">
          <span class="px-3">낰낰 파트너의 계정이 있으신가요?</span><v-btn class="login-font" color="primary" text @click="onOff()">로그인</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email, minLength, sameAs, integer } from 'vuelidate/lib/validators'
import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  data () {
    return {
      partnerName: '',
      email: '',
      phoneNumber: '',
      password: '',
      passwordCheck: ''
    }
  },
  mixins: [validationMixin],
  validations: {
    partnerName: {
      required
    },
    email: {
      required,
      email
    },
    phoneNumber: {
      required,
      integer
    },
    password: {
      required,
      minLength: minLength(6)
    },
    passwordCheck: {
      required,
      sameAs: sameAs('password')
    },
  },
  computed: {
    ...mapState('auth', ['error']),
    partnerNameErrors () {
      const errors = []
      if (!this.$v.partnerName.$dirty) {
        return errors
      };
      !this.$v.partnerName.required && errors.push('대표자명을 입력해주세요.')
      return errors
    },
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) {
        return errors
      };
      !this.$v.email.required && errors.push('이메일을 작성해주세요.')
      !this.$v.email.email && errors.push('이메일 형식으로 작성해주세요.')
      return errors
    },
    phoneNumberErrors () {
      const errors = []
      if (!this.$v.phoneNumber.$dirty) {
        return errors
      };
      !this.$v.phoneNumber.required && errors.push('휴대폰 번호를 입력해주세요.')
      !this.$v.phoneNumber.integer && errors.push('숫자만 입력해주세요.')
      return errors
    },
    passwordErrors () {
      const errors = []
      if (!this.$v.password.$dirty) {
        return errors
      };
      !this.$v.password.required && errors.push('비밀번호를 작성해주세요.')
      !this.$v.password.minLength && errors.push('비밀번호는 최소 6자리 이상입니다.')
      return errors
    },
    passwordCheckErrors () {
      const errors = []
      if (!this.$v.passwordCheck.$dirty) {
        return errors
      };
      !this.$v.passwordCheck.required && errors.push('비밀번호를 한 번 더 입력해주세요.')
      !this.$v.passwordCheck.sameAs && errors.push('입력한 비밀번호가 다릅니다.')
      return errors
    }
  },
  methods: {
    ...mapMutations('auth', ['onOff', 'initError']),
    ...mapActions('auth', ['userSignUp']),
    async signUp () {
      this.$v.$touch()
      if (this.$v.$invalid) {
        console.log('유효성 검사에서 에러가 발견되었습니다.')
      } else {
        var info = {
          email: this.email,
          password: this.password,
          partnerName: this.partnerName,
          phoneNumber: this.phoneNumber
        }
        await this.userSignUp(info)
        if (!this.error) {
          this.onOff()
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
.signup-font {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.Noto-Sans-KR {
  font-family: 'Noto Sans KR', sans-serif;
}
.center {
  display: flex;
  justify-content: center;
}
.pb > div {
  padding-bottom: 15px;
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
.login-font {
  font-weight: 600;
  font-size: 14px;
}
</style>
