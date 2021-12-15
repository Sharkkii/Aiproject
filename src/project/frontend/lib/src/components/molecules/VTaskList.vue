<template>
<div id="v-task-list">
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
</template>

<style lang="scss">
#v-task-list {
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
  name: "VTaskList",
  props: {
    taskList: {
      type: Array,
      default: []
    }
  }
}
</script>