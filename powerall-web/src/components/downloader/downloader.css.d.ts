declare namespace DownloaderCssModule {
  export interface IDownloaderCss {
    anchor: string;
  }
}

declare const DownloaderCssModule: DownloaderCssModule.IDownloaderCss & {
  /** WARNING: Only available when `css-loader` is used without `style-loader` or `mini-css-extract-plugin` */
  locals: DownloaderCssModule.IDownloaderCss;
};

export = DownloaderCssModule;
