<template>
<div id="v-view-monitor">
  <div class="sub-header">
    <p>View Monitor</p>
  </div>
  <div class="task-list">
    <v-task-list v-bind:task-list="taskList">
    </v-task-list>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-view-monitor {
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
</style>

<script>
import VTaskList from "../molecules/VTaskList.vue"
export default {
  name: "VViewMonitor",
  components: {
    VTaskList
  },
  props: {
    taskList: {
      type: Array,
      default: []
    }
  }
}
</script>