import React, { useState, useEffect, useCallback, useRef } from "react";
import { View, StyleSheet, Image } from "react-native";
import Animated from "react-native-reanimated";

export default function LogoScreen() {
  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Animated.Image
        source={require("../../assets/images/logo.png")}
        resizeMode="contain"
        style={{ width: 100, height: 100 }}
      />
    </View>
  );
}
