import React, { useState } from "react";
import { View, Image, TextInput, Button, StyleSheet } from "react-native";
import * as ImagePicker from "expo-image-picker";

// Define props interface
interface PostInputProps {
  value: string;
  onChangeText: (text: string) => void;
  onSubmit: () => void;
  isPosting: boolean;
  previewImage: string | undefined;
  setPreviewImage: (image: string | undefined) => void;
}

// PostInput handles the creation of new posts
// It contains the input field and submit button
export const PostInput: React.FC<PostInputProps> = ({
  value,
  onChangeText,
  onSubmit,
  isPosting,
  previewImage,
  setPreviewImage,
}) => {
  const takePhoto = async () => {
    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== "granted") {
      alert("Permission not granted");
      return;
    }

    const result = await ImagePicker.launchCameraAsync();
    if (!result.canceled) {
      setPreviewImage(result.assets[0].uri);
    }
  };

  return (
    <View style={styles.container}>
      {/* Input field for post content */}
      <TextInput
        style={styles.input}
        value={value}
        onChangeText={onChangeText}
        placeholder="Write your post..."
        // Disable input while posting
        editable={!isPosting}
        multiline
      />

      {/* Submit button with loading state */}
      <View style={{ flexDirection: "row", justifyContent: "space-between" }}>
        <Button
          title={isPosting ? "Posting..." : "Create Post"}
          onPress={onSubmit}
          // Disable button when posting or when input is empty
          disabled={isPosting || !value.trim()}
        />
        <Button title="Take Photo" onPress={takePhoto} />
      </View>
      {previewImage && (
        <Image
          source={{ uri: previewImage }}
          style={{ width: "100%", height: 200, borderRadius: 8 }}
        />
      )}
    </View>
  );
};

// Styles for the PostInput component
const styles = StyleSheet.create({
  // Container for the input section
  container: {
    marginBottom: 20,
    backgroundColor: "#ffffff",
    borderRadius: 8,
    padding: 10,
    // Shadow properties for iOS
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    // Elevation for Android shadow
    elevation: 3,
  },
  // Styling for the text input
  input: {
    borderWidth: 1,
    borderColor: "#e0e0e0",
    borderRadius: 4,
    padding: 12,
    marginBottom: 10,
    minHeight: 100,
    textAlignVertical: "top",
  },
});
