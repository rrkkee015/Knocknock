<template>
  <div class="font">
    <div class="fill-width end">
      <v-btn small text color="primary" @click="goTo()">직접 등록하러 가기<v-icon class="pl-2" small color="primary">fas fa-arrow-right</v-icon></v-btn>
    </div>
    <v-text-field
      class="mt-5"
      label="상호명 검색"
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
    <div class="fill-width center">
      <v-btn color="primary" dark small @click="onSubmit()">검색</v-btn>
    </div>
  </div>  
</template>

<script>
import router from '../../router'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'

import { mapMutations, mapActions } from 'vuex'

export default {
  data () {
    return {
      storeName: ''
    }
  },
  mixins: [validationMixin],
  validations: {
    storeName: {
      required
    }
  },
  computed: {
    storeNameErrors () {
      const errors = []
      if (!this.$v.storeName.$dirty) {
        return errors
      };
      !this.$v.storeName.required && errors.push('상호명을 입력해주세요.')
      return errors
    }
  },
  methods: {
    ...mapMutations('store', ['setIsNew', 'setSearchOn']),
    ...mapActions('store', ['searchStore']),
    onSubmit () {
      this.searchStore(this.storeName)
      this.setSearchOn()
    },
    goTo () {
      this.setIsNew()
      router.push('/store/form')
    }
  }
}
</script>

<style scoped>
.font {
  font-family: 'Noto Sans KR', sans-serif;
}
.center {
  display: flex;
  justify-content: center;
}
.end {
  display: flex;
  justify-content: flex-end;
}
</style>