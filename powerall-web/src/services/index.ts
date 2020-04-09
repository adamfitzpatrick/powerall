import { Ina260Measurement, DateSelection } from "@models"

declare var DATA_HOST: string
declare var DATA_HOST_PORT: string

const URL_BASE =  'http://' + DATA_HOST + ':' + DATA_HOST_PORT
const LOCAL_STORAGE_NAMESPACE = 'powerall-web'
const DATE_STORAGE = `${LOCAL_STORAGE_NAMESPACE}__dates`


export const storeDateSelection = (dateSelection: DateSelection | null) => {
    localStorage.setItem(DATE_STORAGE, JSON.stringify(dateSelection))
}

export const loadDateSelection = (): DateSelection | null => {
    try {
        const data = JSON.parse(localStorage.getItem(DATE_STORAGE)!)
        return { startDate: new Date(data.startDate), endDate: new Date(data.endDate) }
    } catch (e) {
        return null
    }
}

export const load = async (dateSelection: DateSelection | null): Promise<Ina260Measurement[]> => {
    if (dateSelection) {
        return loadRange(dateSelection)
    }
    return loadAll()
}

const loadAll = async (): Promise<Ina260Measurement[]> => {
    return loaderDelegate(URL_BASE)
}

const loadRange = async (dateSelection: DateSelection): Promise<Ina260Measurement[]> => {
    const url = `${URL_BASE}/dates`
    const options = {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(dateSelection)
    }
    return loaderDelegate(url, options)
}

const loaderDelegate = async (url: string, options?: RequestInit): Promise<Ina260Measurement[]> => {
    const response = await fetch(url, options)
    const data = await response.json()
    return data.map((datum: Ina260Measurement) => new Ina260Measurement(datum))
}