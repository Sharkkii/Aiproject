<template>
<div id="v-task-monitor">
  <div class="sub-header">
    <p>Task Monitor</p>
  </div>
  <div class="task-list">
    <v-task-list v-bind:task-list="taskList" v-on:delete-task="deleteTask">
    </v-task-list>
  </div>
</div>
</template>

<style scoped lang="scss">
#v-task-monitor {
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
  name: "VTaskMonitor",
  components: {
    VTaskList
  },
  props: {
    taskList: {
      type: Array,
      default: []
    }
  },
  methods: {
    deleteTask: function(data) {
      this.$emit("delete-task", data)
    }
  }
}
</script>