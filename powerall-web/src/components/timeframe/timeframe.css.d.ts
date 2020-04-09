declare namespace TimeframeCssModule {
  export interface ITimeframeCss {
    content: string;
    datePickerRow: string;
    drawer: string;
    timeframe: string;
  }
}

declare const TimeframeCssModule: TimeframeCssModule.ITimeframeCss & {
  /** WARNING: Only available when `css-loader` is used without `style-loader` or `mini-css-extract-plugin` */
  locals: TimeframeCssModule.ITimeframeCss;
};

export = TimeframeCssModule;
