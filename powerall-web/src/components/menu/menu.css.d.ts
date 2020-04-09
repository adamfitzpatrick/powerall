declare namespace MenuCssModule {
  export interface IMenuCss {
    menu: string;
  }
}

declare const MenuCssModule: MenuCssModule.IMenuCss & {
  /** WARNING: Only available when `css-loader` is used without `style-loader` or `mini-css-extract-plugin` */
  locals: MenuCssModule.IMenuCss;
};

export = MenuCssModule;
