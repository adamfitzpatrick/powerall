declare namespace ChartCssModule {
  export interface IChartCss {
    chart: string;
  }
}

declare const ChartCssModule: ChartCssModule.IChartCss & {
  /** WARNING: Only available when `css-loader` is used without `style-loader` or `mini-css-extract-plugin` */
  locals: ChartCssModule.IChartCss;
};

export = ChartCssModule;
