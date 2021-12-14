<template>
<div id="v-schedule-monitor">
  <div class="sub-header">
    <p>Schedule Monitor</p>
  </div>
  <div class="schedule-list">
    <p>
      Best Schedule: {{ scheduleList }} 
    </p>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-schedule-monitor {
  box-shadow: 0 0 5px $black;
  box-sizing: border-box;
  min-height: 400px;
  padding: 20px;
  width: 800px;
}

.sub-header {
  color: $main-color;
  font-size: 30px;
  font-weight: bold;
}

// .schedule-list {
//   th, td {
//     font-size: 20px;
//     height: 40px;
//     text-align: center;
//     width: 200px;
//   }
// }
</style>

<script>
export default {
  name: "VScheduleMonitor",
  props: {
    scheduleList:{
      type: Object,
      default: {}
    }
  }
}
</script>