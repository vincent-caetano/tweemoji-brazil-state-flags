import React from 'react';
import { Image, type ImageStyle, type StyleProp } from 'react-native';
import type { BrazilStateCode } from '../metadata/states';
const assets = {
  AC: require('../png/144/br-ac.png'),
  AL: require('../png/144/br-al.png'),
  AP: require('../png/144/br-ap.png'),
  AM: require('../png/144/br-am.png'),
  BA: require('../png/144/br-ba.png'),
  CE: require('../png/144/br-ce.png'),
  DF: require('../png/144/br-df.png'),
  ES: require('../png/144/br-es.png'),
  GO: require('../png/144/br-go.png'),
  MA: require('../png/144/br-ma.png'),
  MT: require('../png/144/br-mt.png'),
  MS: require('../png/144/br-ms.png'),
  MG: require('../png/144/br-mg.png'),
  PA: require('../png/144/br-pa.png'),
  PB: require('../png/144/br-pb.png'),
  PR: require('../png/144/br-pr.png'),
  PE: require('../png/144/br-pe.png'),
  PI: require('../png/144/br-pi.png'),
  RJ: require('../png/144/br-rj.png'),
  RN: require('../png/144/br-rn.png'),
  RS: require('../png/144/br-rs.png'),
  RO: require('../png/144/br-ro.png'),
  RR: require('../png/144/br-rr.png'),
  SC: require('../png/144/br-sc.png'),
  SP: require('../png/144/br-sp.png'),
  SE: require('../png/144/br-se.png'),
  TO: require('../png/144/br-to.png'),
} as const;
export function StateFlag({ state, size = 24, style }: {
  state: BrazilStateCode; size?: number; style?: StyleProp<ImageStyle>;
}) {
  return <Image source={assets[state]} accessibilityLabel={`Bandeira: ${state}`}
    resizeMode="contain" style={[{ width: size, height: size }, style]} />;
}
