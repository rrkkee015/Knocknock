<template>
  <div class="font">
    <v-col cols="12" class="register-head">영업장 등록</v-col>
    <v-col>
      <v-text-field
        label="사업자 성명"
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
        label="상호명"
        v-model="storeName"
        :error-messages="storeNameErrors"
        @input="$v.storeName.$touch()"
        @blur="$v.storeName.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
      <v-text-field
        label="사업장 주소"
        v-model="address"
        :error-messages="addressErrors"
        @input="$v.address.$touch()"
        @blur="$v.address.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
      <v-text-field
        label="사업 등록번호"
        v-model="regiNumber"
        :error-messages="regiNumberErrors"
        @input="$v.regiNumber.$touch()"
        @blur="$v.regiNumber.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
    </v-col>
    <v-col class="center pt-4" cols="12">
      <v-btn x-large color="primary" @click="onSubmit()">나의 사업장 요청하기</v-btn>
    </v-col>
    <div>
      <v-col class="center-also-align bottom-position fill-width">
        <v-icon color="primary">fas fa-exclamation</v-icon><span class="px-2 footer-text">사업장 등록에는 영업일 기준 하루가 소요됩니다.</span><v-icon color="primary">fas fa-exclamation</v-icon>
      </v-col>
    </div>
  </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'

import router from '../router'

import { mapState, mapMutations, mapActions } from 'vuex'

export default {
  data () {
    return {
      storeName: '',
      partnerName: '',
      address: '',
      regiNumber: '',
    }
  },
  mixins: [validationMixin],
  validations: {
    storeName: {
      required
    },
    partnerName: {
      required
    },
    address: {
      required
    },
    regiNumber: {
      required
    }
  },
  computed: {
    ...mapState('store', ['isNew', 'storeId']),
    storeNameErrors () {
      const errors = []
      if (!this.$v.storeName.$dirty) {
        return errors
      };
      !this.$v.storeName.required && errors.push('상호명을 입력해주세요.')
      return errors
    },
    partnerNameErrors () {
      const errors = []
      if (!this.$v.partnerName.$dirty) {
        return errors
      };
      !this.$v.partnerName.required && errors.push('사업자 성명을 입력해주세요.')
      return errors
    },
    addressErrors () {
      const errors = []
      if (!this.$v.address.$dirty) {
        return errors
      };
      !this.$v.address.required && errors.push('사업장 주소를 입력해주세요.')
      return errors
    },
    regiNumberErrors () {
      const errors = []
      if (!this.$v.regiNumber.$dirty) {
        return errors
      };
      !this.$v.regiNumber.required && errors.push('사업 등록번호를 입력해주세요.')
      return errors
    }
  },
  methods: {
    ...mapMutations('store', ['initStoreId']),
    ...mapActions('store', ['enrollStore']),
    async onSubmit () {
      const params = {
        // is_new: this.isNew,
        store_id: this.storeId,
        company_name: this.storeName,
        business_registration_number: this.regiNumber,
        representative_name: this.partnerName,
        business_address: this.address,
        // registration_image: this.file
      }
      await this.enrollStore(params)
      this.initStoreId()
      router.push('/store')
    }
  },
  beforeRouteEnter(to, from, next) {
    if (from.path === '/') {
      next('/store/register')
    } else {
      next()
    }
  }
}
</script>

<style scoped>
.font {
  font-family: 'Noto Sans KR', sans-serif;
}
.register-head {
  font-size: 60px;
  font-weight: 900;
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
</style>