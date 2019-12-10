<template>
  <v-col class="total-size">
    <div class="menu-head">
      <p class="menu-title pr-4">메뉴</p>
      <p class="menu-add" @click="newMenu()">추가하기</p>
      <p class="menu-delete pl-4" @click="deleteButtonOnOff()">삭제하기</p>
    </div>
    <newMenuBox 
      v-show="newMenuBoxToggle"
      @turnNewMenuBoxToggle="newMenuBoxToggle=false"
    />
    <div class="menu-detail-category">
      <v-col v-if="!allMenus.length" class="pa-0">
        사장님 ! 메뉴를 등록해주세요. (˃︿˂)
      </v-col>
      <v-col v-for="(menu,i) in allMenus" :key="i" cols="12" class="menu-detail pb-2">
        <v-col cols="8" class="menu-tag">{{ menu.name }}</v-col>
        <v-col v-if="!deleteButton" cols="1"></v-col>
        <v-col cols="3">{{ menu.price }}원</v-col>
        <v-col v-if="deleteButton">
          <v-icon @click="deleteCheckOn(menu.id)" class="fas fa-times" small></v-icon>
        </v-col>
      </v-col>
    </div>
    <v-dialog
      v-model="deleteCheck"
      max-width="290"
    >
      <v-card class="text-center">
        <p class="pt-5 info-text">
          <span>메뉴를 삭제하시겠습니까?</span>
        </p>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="info-text"
            color="blue darken-3"
            text
            @click="deleteCheck = false"
          >
            닫기
          </v-btn>
          <v-btn
            class="info-text"
            color="blue darken-3"
            text
            @click="deleteMenuOn(menuId)"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-col>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import newMenuBox from './newMenuBox'

export default {
  components: {
    newMenuBox
  },
  computed: {
    ...mapState('store', ['allMenus'])
  },
  data () {
    return {
      newMenuBoxToggle: false,
      deleteButton: false,
      deleteCheck: false,
      menuId: 0
    }
  },
  async created () {
    await this.getAllMenus(this.$route.params.storeId)
  },
  methods: {
    ...mapActions('store', ['getAllMenus']),
    ...mapActions('menu', ['deleteMenu']),
    newMenu () {
      this.newMenuBoxToggle = !this.newMenuBoxToggle
    },
    deleteButtonOnOff () {
      this.deleteButton = !this.deleteButton
    },
    async deleteMenuOn (menuId) {
      if (this.menuId === 0) {
        console.log("잘못 된 형식입니다.")
      } else {
        await this.deleteMenu(menuId)
        await this.getAllMenus(this.$route.params.storeId)
        this.deleteCheck = false
      }
    },
    deleteCheckOn (menuId) {
      this.menuId = menuId
      this.deleteCheck = true
    }
  }
}
</script>

<style scoped>
.total-size {
  min-height: 700px;
}
.menu-head {
  display: flex;
  align-items: flex-end;
}
.menu-add {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  color: #0091EA;
  font-weight: 500;
}
.menu-delete {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  color: #D32F2F;
  font-weight: 500;
}
.menu-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.menu-detail-category {
  font-family: 'Noto Sans KR', sans-serif;
  margin-bottom: 16px;
}
.menu-tag {
  color: black;
}
.menu-detail {
  display: flex;
  padding: 0px;
  color: #a9a9a9;
}
.menu-detail > div {
  padding: 0px;
}
.info-text {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
