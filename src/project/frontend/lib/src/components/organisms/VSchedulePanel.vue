<template>
<div id="v-schedule-panel">
  <div class="sub-header">
    <p>Schedule Panel</p>
  </div>
  <v-schedule-button v-on:get-best-schedule="getBestSchedule">
  </v-schedule-button>
</div>
</template>

<style scoped lang="scss">
#v-schedule-panel {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  padding: 20px;
  width: 600px;
}

.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}
</style>

<script>
import VScheduleButton from "../molecules/VScheduleButton.vue"
export default {
  name: "VSchedulePanel",
  components: {
    VScheduleButton
  },
  methods: {
    getBestSchedule: function(data) {
      this.$emit("get-best-schedule", data)
    }
  }
}
</script>