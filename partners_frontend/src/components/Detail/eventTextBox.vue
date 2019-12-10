<template>
  <div class="mt-5">
    <div class="event-layout mb-4">
      <div class="pa-5">
        <p class="event-title mb-0">제목</p>
        <v-text-field
          class="text-area-font"
          v-model="eventTitle"
        >
        </v-text-field>
        <p class="event-title mb-0">내용</p>
        <v-textarea
          class="text-area-font"
          v-model="eventContent"
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
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      newevent: '',
      newTitle: ''
    }
  },
  computed: {
    eventTitle: {
      get () {
        return this.$store.state.postEvent.eventTitle
      },
      set (title) {
        this.newTitle = title
      }
    },
    eventContent: {
      get () {
        return this.$store.state.postEvent.eventContent
      },
      set (content) {
        this.newevent = content
      }
    }
  },
  methods: {
    ...mapMutations('eventEvent', ['changeTextBox', 'changeContent']),
    submit () {
      this.changeTextBox()
      this.changeContent(this.newevent)
    }
  }
}
</script>

<style scoped>
.event-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.event-title {
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
