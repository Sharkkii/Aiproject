<template>
<div id="v-schedule-monitor">
  <div class="sub-header">
    <p>Schedule Monitor</p>
  </div>
  <div class="schedule-list">
    <div>
      <p>Best Schedule</p>
    </div>
    <div v-for="schedule in scheduleList" v-bind:key="schedule.id">
      <span v-for="action in schedule" v-bind:key="action.id">
        {{ action }} ->
      </span>
    </div>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-schedule-monitor {
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
  data: function() {
    return {
      scheduleList: []
    }
  },
  props: {
    nSlot: {
      type: Number,
      default: null
    },
    nWorker: {
      type: Number,
      default: null
    },
    scheduleListProperty: {
      type: Array,
      default: []
    }
  },
  watch: {
    scheduleListProperty: function() {
      console.log(this.scheduleListProperty)
      this.scheduleList = this.scheduleListProperty
    }
  }
}
</script>