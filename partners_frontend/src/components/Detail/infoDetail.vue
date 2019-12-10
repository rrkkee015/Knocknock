<template>
  <v-col class="total-size">
    <div class="info-head">
      <p class="info-title pr-4 mb-0">가게 소개</p>
      <p class="info-modify mb-0" @click="toggling('descrip')">수정하기</p>
    </div>
    <p v-if="!data.description" cols="11" class="pa-0 info-description">
      사장님 ! 가게 소개를 작성해주세요. (˃︿˂)
    </p>
    <p v-if="!descripEdit" class="info-description">
      {{ data.description }}
    </p>
    <div v-else class="mb-5">
      <v-textarea
        class="text-area"
        v-model="data.description"
        auto-grow
      >
      </v-textarea>
      <div class="fill-width btn-layout">
        <v-btn
          color="primary"
          dark
          small
          @click="submit()"
        >작성 완료</v-btn>
      </div>
    </div>
    <p class="info-title">사업자 정보</p>
    <div class="info-detail-category">
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">대표자명</v-col>
        <v-col cols="8">{{ randomOwner }}</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">상호명</v-col>
        <v-col cols="8">{{ data.storeName }}</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">사업자 주소</v-col>
        <v-col cols="8">{{ data.roadAddr }}</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">사업자 번호</v-col>
        <v-col cols="8">609-04-76324</v-col>
      </v-col>
    </div>
    <div class="info-head">
      <p class="info-title pr-4">영업 시간</p>
      <p class="info-modify">수정하기</p>
    </div>
    <div class="week-time">
      <p v-for="(date, i) in data.business_hours" :key="i">
				<span class="info-tag">{{ date.day }} - </span>
				<span class="holiday" v-if="date.start === null && date.end === null">쉬는 날이에요 ~</span>
				<span class="work-time" v-else>{{ date.start.slice(0, 5) }} ~ {{ date.end.slice(0, 5) }}</span>
				<br>
				<span v-if="date.start_break !== null || date.end_break !== null">쉬는 시간 - {{ date.start_break.slice(0, 5) }} ~ {{ date.end_break.slice(0, 5) }}</span>
				<br>
				<span v-if="date.last_order" class="last-order">마지막 주문 - {{ date.last_order.slice(0, 5) }}</span>
			</p>
    </div>
    <div class="info-head">
      <p class="info-title pr-4">매장 정보</p>
      <p class="info-modify">수정하기</p>
    </div>

    <div class="info-detail-category">
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">업종</v-col>
        <v-col cols="8" class="pl-2">{{ data.mainCategory }}</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">카테고리</v-col>
        <v-col cols="8" class="pl-2">{{ data.subCategory }}</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">연락처</v-col>
        <v-col cols="8" class="pl-2">{{ data.contact }}</v-col>
      </v-col>
      <v-col v-for="option in totalOptions" :key="option.key" cols="12" class="info-detail pb-2">				
        <v-col cols="4" class="info-tag">{{ option }}</v-col>
        <v-col v-if="possibleOptions.includes(option)" cols="8" class="pl-2 possible-text">가능</v-col>
        <v-col v-else cols="8" class="pl-2 impossible-text">불가</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">가격대</v-col>
        <v-col v-if="data.priceAvg" cols="8">{{ data.priceAvg }} 원</v-col>
        <v-col v-else cols="8">가격대를 등록해주세요.</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">네이버 리뷰 수</v-col>
        <v-col v-if="data.reviewCnt" cols="8">{{ data.reviewCnt }} 개</v-col>
				<v-col v-else>네이버 리뷰가 존재하지 않습니다.</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">태그</v-col>
        <v-col cols="8">{{ data.tags }}</v-col>
      </v-col>
    </div>
  </v-col>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  props: {
    data: {
      type: Object,
      default: {}
    }
  },
  data () {
    return {
      descripEdit: false
    }
	},
  computed: {
		...mapState('store', ['oneStore', 'totalOptions', 'possibleOptions']),
		randomOwner () {
			var arr = ['강민수', '한동훈', '이혜희', '강성진', '이민영']
			return arr[Math.floor(Math.random() * arr.length)]
		}
  },
  methods: {
    ...mapActions('store', ['editStoreDescrip']),
    toggling (toggle) {
      if (toggle === 'descrip') {
        this.descripEdit = !this.descripEdit
      }
    },
    submit () {
      var params = {
        id: this.data.id,
        description: this.data.description
      }
      this.editStoreDescrip(params)
      this.descripEdit = !this.descripEdit
    }
  }
}
</script>

<style scoped>
.last-order {
	color: #D32F2F;
}
.work-time {
	color: #00BFA5;
}
.holiday {
	color: #0091EA;
}
.text-area {
  font-family: 'Noto Sans KR', sans-serif;
}
.total-size {
  min-height: 700px;
}
.info-head {
  display: flex;
  align-items: flex-end;
}
.info-modify {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #0091EA;
}
.info-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.info-description {
  white-space: pre-line;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  color: #a9a9a9;
}
.week-time {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  color: #a9a9a9;
  margin-bottom: 16px;
}
.week-time > p {
  margin-bottom: 0px;
}
.sunday-time-text {
  color: #D50000;
}
.break-time-text {
  color: #00BFA5;
  display: flex;
}
.last-order-text {
  color: #00BFA5;
  display: flex;
}
.icon-scale {
  transform: scale(0.8)
}
.icon-width {
  display: flex;
  justify-content: center;
  width: 40px;
}
.info-detail-category {
  font-family: 'Noto Sans KR', sans-serif;
  margin-bottom: 16px;
}
.info-detail {
  display: flex;
  padding: 0px;
  color: #a9a9a9;
}
.info-detail > div {
  padding: 0px;
}
.info-tag  {
  color: black;
}
.possible-text {
  color:#0091EA;
}
.impossible-text {
  color:#D50000
}
.btn-layout {
  display: flex;
  justify-content: flex-end;
}
</style>
