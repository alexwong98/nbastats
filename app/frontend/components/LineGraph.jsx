import React, { Component } from 'react'
import { Line } from 'react-chartjs-2'
import { defaults } from 'react-chartjs-2'

class LineGraph extends Component {

  render() {
    if (this.props.data) {

      let largest_x = []
      let datasets = this.props.data.map((dataset) => {
        if (dataset.x.length > largest_x.length) {
            largest_x = dataset.x
        }
        return {
          label: dataset['name'],
          fill: false,
          lineTension: 0.1,
          backgroundColor: 'rgba(75,192,192,0.4)',
          borderColor: 'rgba(75,192,192,1)',
          borderCapStyle: 'butt',
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: dataset['y'],
          responsive : true,
          responsiveAnimationDuration : 1000
        }
      })


      defaults.global.animation.duration = 2000

      var data = {
        labels: largest_x, 
        datasets: datasets
      };

      console.log(datasets)
      return <Line data={data} />
    }
  }
    
}

export default LineGraph