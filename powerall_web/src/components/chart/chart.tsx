import * as React from 'react'
import * as moment from 'moment'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Label } from 'recharts'

import { Ina260Measurement } from '@models'
import { load } from '@services'

type DataType = Ina260Measurement[] | null

const tickFormatter = (time: number) => moment(time).format('hh:mm')

const tooltipLabelFormatter = (time: number) => {
    console.log(moment().utcOffset())
    return moment(time).format('MMM DD YYYY HH:mm')
}

const formatterInvestigator = (value: string, entry: string, index: number) => {
    console.log(value, entry, index)
    return <div>no</div>
}

const style = {
    position: 'fixed',
    width: '75vw',
    height: '75vh',
    top: '12.5vh',
    left: '12.5vw'
} as React.CSSProperties

export function Chart () {
    const [data, setData] = React.useState<DataType>(null)
    if (!data) {
        load().then(response => setData(response))
        return null
    }
    console.log(data)

    return (
        <div style={style}>
            <LineChart
                width={0.75 * window.innerWidth}
                height={0.75 * window.innerHeight}
                data={data}
                margin={{
                    top: 5, right: 30, left: 20, bottom: 5,
                }}
            >
                <CartesianGrid strokeDasharray='3 3' />
                <XAxis
                    dataKey='time'
                    scale='time'
                    type='number'
                    domain={['dataMin', 'auto']}
                    tickFormatter={tickFormatter}
                />
                <YAxis yAxisId='left' domain={[0, 'auto']} dataKey='voltage'>
                    <Label value='volt' angle={-90} position='left' />
                </YAxis>
                <YAxis yAxisId='right' domain={[0, 'auto']} dataKey='current' orientation='right'>
                    <Label value='ampere' angle={90} position='right' />
                </YAxis>
                <Tooltip labelFormatter={tooltipLabelFormatter} />
                <Legend />
                <Line yAxisId='left' type='linear' dataKey='voltage' stroke='#8884d8' activeDot={{ r: 8 }} />
                <Line yAxisId='right' type='linear' dataKey='current' stroke='#82ca9d' activeDot={{ r: 8 }} />
            </LineChart>
        </div>
    )
}