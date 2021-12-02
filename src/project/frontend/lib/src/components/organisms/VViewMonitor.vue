<template>
<div id="v-view-monitor">
  <div class="sub-header">
    <p>View Monitor</p>
  </div>
  <div class="task-list">
    <table>
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Required Effort</th>
          <th>Remaining Time</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in taskList" v-bind:key="task.id">
          <td>{{ task.name }}</td>
          <td>{{ task.required_effort }}</td>
          <td>{{ task.remaining_time }}</td>
          <td>
            <button>Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
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

.task-list {
  th, td {
    font-size: 20px;
    height: 40px;
    text-align: center;
    width: 200px;
  }
}
</style>

<script>
export default {
  name: "VViewMonitor",
  props: [
    "taskList"
  ]
}
</script>