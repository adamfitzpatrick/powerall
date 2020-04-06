export type SourceType = 'SOLAR' | 'WIND' | 'OTHER'

export class Ina260Measurement {
    constructor(data: Ina260Measurement) {
        this.time = new Date(data.timestamp).getTime()
        Object.assign(this, data)
    }

    time: number
    timestamp: string
    source_name: string
    source_type: SourceType
    voltage: number
    currenct: number
}