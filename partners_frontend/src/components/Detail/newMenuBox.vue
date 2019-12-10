<template>
  <div class="mt-5">
    <div class="newMenu-layout mb-4">
      <div class="pa-5">
        <p class="newMenu-title mb-0">제목</p>
        <v-text-field
          class="text-area-font"
          v-model="newMenuTitle"
          label="예) 아메리카노"
        >
        </v-text-field>
        <p class="newMenu-title mb-0">가격</p>
        <v-text-field
          class="text-area-font"
          v-model="newMenuContent"
          type="Number"
          label="예) 4500"
        >
        </v-text-field>
        <div class="fill-width btn-layout">
          <v-btn
            color="primary"
            dark
            small
            @click="submit()"
          >작성 완료</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      newMenuTitle: '',
      newMenuContent: ''
    }
  },
  methods: {
    ...mapActions('store', ['getAllMenus']),
    ...mapActions('menu', ['postMenu']),
    async submit () {
      var params = {
        name: this.newMenuTitle,
				price: this.newMenuContent,
        store: this.$route.params.storeId
      }
			await this.postMenu(params)
			this.getAllMenus(this.$route.params.storeId)
			this.newMenuTitle = ''
			this.newMenuContent = ''
      this.$emit('turnNewMenuBoxToggle')
    }
  }
}
</script>

<style scoped>
.newMenu-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.newMenu-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  font-weight: 700;
}
.btn-layout {
  display: flex;
  justify-content: flex-end;
}
.text-area-font {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>