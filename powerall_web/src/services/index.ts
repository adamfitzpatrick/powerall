import { Ina260Measurement } from "@models"

declare var DATA_HOST: string
declare var DATA_HOST_PORT: string

export const load = async (): Promise<Ina260Measurement[]> => {
    const url = 'http://' + DATA_HOST + ':' + DATA_HOST_PORT
    const response = await fetch(url)
    const data = await response.json()
    return data.map((datum: Ina260Measurement) => new Ina260Measurement(datum))
}