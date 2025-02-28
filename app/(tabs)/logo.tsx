import React, { useState, useEffect, useCallback, useRef } from "react";
import { View, StyleSheet, Image } from "react-native";
import { Gesture, GestureDetector } from "react-native-gesture-handler";
import Animated, {
  useAnimatedStyle,
  useSharedValue,
  withSpring,
} from "react-native-reanimated";

const imageSize = 100;

export default function LogoScreen() {
  const scaleImage = useSharedValue(imageSize);
  const translateX = useSharedValue(0);
  const translateY = useSharedValue(0);

  const doubleTap = Gesture.Tap()
    .numberOfTaps(2)
    .onStart(() => {
      if (scaleImage.value !== imageSize * 2) {
        scaleImage.value = scaleImage.value * 2;
      } else {
        scaleImage.value = Math.round(scaleImage.value / 2);
      }
    });

  const imageStyle = useAnimatedStyle(() => {
    return {
      width: withSpring(scaleImage.value),
      height: withSpring(scaleImage.value),
    };
  });

  const drag = Gesture.Pan().onChange((event) => {
    translateX.value += event.changeX;
    translateY.value += event.changeY;
  });

  const containerStyle = useAnimatedStyle(() => {
    return {
      transform: [
        {
          translateX: translateX.value,
        },
        {
          translateY: translateY.value,
        },
      ],
    };
  });

  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <GestureDetector gesture={drag}>
        <GestureDetector gesture={doubleTap}>
          <Animated.Image
            source={require("../../assets/images/logo.png")}
            resizeMode="contain"
            style={[
              imageStyle,
              containerStyle,
              { width: imageSize, height: imageSize },
            ]}
          />
        </GestureDetector>
      </GestureDetector>
    </View>
  );
}
